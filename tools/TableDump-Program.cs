using System.Reflection;
using Microsoft.Extensions.Options;
using NexusUnleashed.Game.Static;
using NexusUnleashed.GameTable;
using NexusUnleashed.GameTable.Configuration.Model;
using NexusUnleashed.GameTable.Model;

namespace NexusUnleashed.TableDump
{
    /// <summary>
    /// Dumps id and name pairs out of the client game tables.
    /// </summary>
    /// <remarks>
    /// Names live in the .tbl files behind a localised text id, so nothing outside the running server could resolve
    /// one. That made every "which creature is this" and "is this really a Spell4 id" question unanswerable from a
    /// shell, and it is the step that blocks turning harvested reference data into anything usable.
    ///
    /// Deliberately outside Source and out of the solution: it is a workshop tool, not part of the server, and it
    /// must not end up in a deployed image.
    ///
    /// Usage: NexusUnleashed.TableDump &lt;tbl directory&gt; &lt;output directory&gt;
    /// </remarks>
    public static class Program
    {
        public static async Task<int> Main(string[] args)
        {
            if (args.Length >= 3 && args[1] == "--inspect")
                return await Inspect(args[0], args[2], args.Length > 3 ? args[3] : null);

            // --find exists because --inspect can only reach a row whose Id you already know, and the rows
            // worth reading are usually the ones you cannot name. Spell4Effects is the case that forced it:
            // damage scaling lives there, keyed by SpellId, and there is no way to get from "Mind Burst" to
            // its effect rows without filtering on a field that is not the primary key.
            if (args.Length >= 5 && args[1] == "--find")
                return await Inspect(args[0], args[2], null, args[3], args[4]);

            // --all dumps EVERY table there is a model for, not the seven someone thought to hand-write.
            //
            // 384 .tbl files sit beside 385 model classes: the schemas were already written and the dumper
            // simply never loaded them, so 377 tables were unreachable from a shell for no reason other than
            // nobody having typed their names. That is the same shape as the spell4effects block that was
            // written, never registered with the loader, and printed "the table did not load" on every run
            // while looking implemented.
            //
            // Reflection over GameTableManager's GameTable<T> properties means a new model class is dumpable
            // the moment it exists, with no second place to update.
            if (args.Length >= 3 && args[1] == "--all")
                return await DumpAll(args[0], args[2], args.Length > 3 ? args[3] : null);

            if (args.Length < 2)
            {
                Console.Error.WriteLine("usage: NexusUnleashed.TableDump <tbl directory> <output directory>");
                Console.Error.WriteLine("       NexusUnleashed.TableDump <tbl directory> --inspect <table> [id]");
                Console.Error.WriteLine("       NexusUnleashed.TableDump <tbl directory> --find <table> <field> <value>");
                Console.Error.WriteLine("       NexusUnleashed.TableDump <tbl directory> --all <output directory> [name filter]");
                return 1;
            }

            string tablePath  = args[0];
            string outputPath = args[1];

            if (!Directory.Exists(tablePath))
            {
                Console.Error.WriteLine($"tbl directory does not exist: {tablePath}");
                return 1;
            }

            Directory.CreateDirectory(outputPath);

            var manager = new GameTableManager(Options.Create(new GameTableConfig
            {
                GameTablePath = tablePath
            }));

            // only what is needed, because the English text table alone is large and loading everything to answer a
            // name lookup takes minutes
            await manager.Initialise(new GameTableLoader()
                .AddTextTable(Language.English)
                .AddGameTable<Creature2Entry>()
                .AddGameTable<Spell4Entry>()
                .AddGameTable<Spell4BaseEntry>()
                // The spell4effects dump block below was written without this line, so the table was
                // never loaded and every run printed "skipped - the table did not load" and carried
                // on. The dump looked implemented; it produced nothing. Same shape as a handler
                // registered for an event that never fires.
                .AddGameTable<Spell4EffectsEntry>()
                .AddGameTable<Quest2Entry>()
                .AddGameTable<WorldEntry>()
                .AddGameTable<MapZoneEntry>()
                .AddGameTable<WorldZoneEntry>());

            TextTable text = manager.TextEnglish;
            if (text == null)
            {
                Console.Error.WriteLine("the English text table did not load, so no name can be resolved");
                return 1;
            }

            // CreationTypeEnum is what the world database's entity.type column was generated from - it is the
            // client's own idea of what kind of thing a creature is, and it does not line up with the server's
            // EntityType enum at every value.
            // tier, difficulty and archetype are what Jabbithole shows as a creature's rank (Minion, Grunt, Fodder,
            // Challenger, Superior, Prime). Carrying them here is what lets the join learn the rank mapping from the
            // rows whose identity is already certain, and then use it to break ties on the ones that are not.
            Write(Path.Combine(outputPath, "creature2.tsv"),
                "id\tname\tcreationType\tmodelInfoId\ttierId\tdifficultyId\tarchetypeId\traceId\tdescription",
                manager.Creature2, e => string.Join('\t',
                    e.Id,
                    Clean(text.GetEntry(e.LocalizedTextIdName)),
                    e.CreationTypeEnum,
                    e.Creature2ModelInfoId,
                    e.Creature2TierId,
                    e.Creature2DifficultyId,
                    e.Creature2ArcheTypeId,
                    e.UnitRaceId,
                    Clean(e.Description)));

            Write(Path.Combine(outputPath, "spell4.tsv"), "id\tname\tspell4BaseId\ttier",
                manager.Spell4, e => $"{e.Id}\t{Clean(NameOfSpell(manager, text, e))}\t{e.Spell4BaseIdBaseSpell}\t{e.TierIndex}");

            // Spell4Effects is where damage actually comes from, and it is why --find exists.
            // ParameterType and ParameterValue together ARE the scaling: a spell states how much it
            // gains per point of Assault Power, per point of Support Power, per level. Those
            // coefficients are PER ABILITY and vary widely - measured across seven Esper abilities
            // they ran from 0.125 to 0.5203, a four-fold spread - so there is no single scaling
            // number for the game, and any tool implying one is wrong.
            //
            // Dumped whole rather than queried per spell, because a per-spell lookup reloads the
            // entire table on every call and turns a few hundred abilities into half an hour.
            Write(Path.Combine(outputPath, "spell4effects.tsv"),
                "id	spellId	effectType	damageType	parameterTypes	parameterValues	dataBits00",
                manager.Spell4Effects, e =>
                    $"{e.Id}	{e.SpellId}	{e.EffectType}	{e.DamageType}	"
                    + $"{string.Join(",", e.ParameterType)}	{string.Join(",", e.ParameterValue)}	"
                    + $"{e.DataBits00}");

            Write(Path.Combine(outputPath, "quest2.tsv"), "id\tname",
                manager.Quest2, e => $"{e.Id}\t{Clean(text.GetEntry(e.LocalizedTextIdTitle))}");

            // World is what answers "which worlds exist and can the server actually load them" - AssetPath names the
            // .nfmap the server needs on disk, so this dump crossed against the map folder and against worlddb.entity
            // is what tells you which worlds are visitable, which are populated, and which are neither. Most rows
            // have no LocalizedTextIdName, so the asset path is usually the only human readable handle a world has.
            Write(Path.Combine(outputPath, "world.tsv"), "id\tname\tassetPath\ttype",
                manager.World, e => $"{e.Id}\t{Clean(text.GetEntry(e.LocalizedTextIdName))}\t{Clean(e.AssetPath)}\t{e.Type}");

            // Only 25 worlds carry a name of their own, and they are the instances. Every open world zone name lives
            // in MapZone against the zone id the server already resolves per position out of the .nfmap zone data,
            // so this is what turns "world 22 zone 2770" into somewhere a person recognises.
            Write(Path.Combine(outputPath, "mapzone.tsv"), "id\tname\tcontinentId\tfolder",
                manager.MapZone, e => $"{e.Id}\t{Clean(text.GetEntry(e.LocalizedTextIdName))}\t{e.MapContinentId}\t{Clean(e.Folder)}");

            // WorldZone, not MapZone, is what the ids coming out of the .nfmap zone data refer to - MapZone is the
            // world map UI's own list and only answered 1 of the 6 zone ids seen live. This is the table that turns
            // a zone id in a log line into a place name.
            Write(Path.Combine(outputPath, "worldzone.tsv"), "id\tname\tparentZoneId",
                manager.WorldZone, e => $"{e.Id}\t{Clean(text.GetEntry(e.LocalizedTextIdName))}\t{e.ParentZoneId}");

            return 0;
        }

        /// <summary>
        /// Print every field of one table's rows, so a question about a specific row can be answered without
        /// guessing which columns matter in advance.
        /// </summary>
        /// <remarks>
        /// The dump modes above are deliberately narrow - id and name - because that is what bulk work needs. This
        /// is the other half: when one entity is behaving oddly, print the whole row and look.
        /// </remarks>
        /// <summary>
        /// Dump every table a model class exists for, discovered by reflection.
        /// </summary>
        /// <remarks>
        /// Tables are loaded in batches rather than all at once: the full set is hundreds of megabytes and
        /// loading everything before writing anything means a failure at table 300 loses the first 299.
        /// Each batch is written before the next is loaded, so a partial run still leaves usable output.
        ///
        /// Array fields are joined with commas rather than skipped. They are where the interesting data
        /// lives - Spell4Effects.ParameterType[] and ParameterValue[] ARE the damage scaling model - and a
        /// dumper that quietly drops them produces a file that looks complete and answers nothing.
        /// </remarks>
        private static async Task<int> DumpAll(string tablePath, string outputPath, string filter)
        {
            if (!Directory.Exists(tablePath))
            {
                Console.Error.WriteLine($"tbl directory does not exist: {tablePath}");
                return 1;
            }

            Directory.CreateDirectory(outputPath);

            List<PropertyInfo> tables = typeof(GameTableManager)
                .GetProperties(BindingFlags.Public | BindingFlags.Instance)
                .Where(p => p.PropertyType.IsGenericType
                         && p.PropertyType.GetGenericTypeDefinition() == typeof(GameTable<>))
                .Where(p => filter == null || p.Name.Contains(filter, StringComparison.OrdinalIgnoreCase))
                .OrderBy(p => p.Name)
                .ToList();

            Console.WriteLine($"{tables.Count} table(s) with a model class"
                + (filter != null ? $" matching '{filter}'" : "") + Environment.NewLine);

            int written = 0, skipped = 0;
            long totalRows = 0;

            const int batchSize = 24;
            for (int offset = 0; offset < tables.Count; offset += batchSize)
            {
                List<PropertyInfo> batch = tables.Skip(offset).Take(batchSize).ToList();

                var manager = new GameTableManager(Options.Create(new GameTableConfig
                {
                    GameTablePath = tablePath
                }));

                var loader = new GameTableLoader();
                MethodInfo add = typeof(GameTableLoader).GetMethod(nameof(GameTableLoader.AddGameTable));
                foreach (PropertyInfo table in batch)
                    add.MakeGenericMethod(table.PropertyType.GetGenericArguments()[0]).Invoke(loader, null);

                try
                {
                    await manager.Initialise(loader);
                }
                catch (Exception e)
                {
                    // One unreadable table must not cost the other twenty-three, and the first attempt at
                    // this DID cost them: a single table with no file on disk threw during Initialise and
                    // 24 tables were reported "skipped" when 23 of them were fine. Retry the batch one at a
                    // time so the failure is isolated to the table that actually caused it.
                    Console.Error.WriteLine($"  batch at {offset} failed ({e.Message}) - retrying individually");

                    foreach (PropertyInfo one in batch)
                    {
                        var solo = new GameTableManager(Options.Create(new GameTableConfig
                        {
                            GameTablePath = tablePath
                        }));
                        var soloLoader = new GameTableLoader();
                        typeof(GameTableLoader).GetMethod(nameof(GameTableLoader.AddGameTable))
                            .MakeGenericMethod(one.PropertyType.GetGenericArguments()[0])
                            .Invoke(soloLoader, null);

                        try
                        {
                            await solo.Initialise(soloLoader);
                        }
                        catch (Exception inner)
                        {
                            Console.Error.WriteLine($"  UNREADABLE {one.Name}: {inner.Message}");
                            skipped++;
                            continue;
                        }

                        int rows = Write(solo, one, outputPath);
                        if (rows < 0) skipped++; else { written++; totalRows += rows; }
                    }

                    continue;
                }

                foreach (PropertyInfo table in batch)
                {
                    int rows = Write(manager, table, outputPath);
                    if (rows < 0) skipped++; else { written++; totalRows += rows; }
                }
            }

            Console.WriteLine($"{Environment.NewLine}{written} table(s) written, {skipped} skipped, {totalRows:N0} rows total");
            return 0;
        }

        /// <summary>
        /// Write one loaded table to TSV. Returns the row count, or -1 if it did not load.
        /// </summary>
        private static int Write(GameTableManager manager, PropertyInfo table, string outputPath)
        {
            object value = table.GetValue(manager);
            if (value == null)
            {
                Console.Error.WriteLine($"  skipped {table.Name} - the table did not load");
                return -1;
            }

            Type entry = table.PropertyType.GetGenericArguments()[0];
            FieldInfo[] fields = entry.GetFields(BindingFlags.Public | BindingFlags.Instance);
            var rows = (System.Collections.IEnumerable)value.GetType().GetProperty("Entries").GetValue(value);

            string path = Path.Combine(outputPath,
                char.ToLowerInvariant(table.Name[0]) + table.Name[1..] + ".tsv");

            using var writer = new StreamWriter(path);
            writer.WriteLine(string.Join('\t', fields.Select(f => f.Name)));

            int count = 0;
            foreach (object row in rows)
            {
                writer.WriteLine(string.Join('\t', fields.Select(f => Cell(f.GetValue(row)))));
                count++;
            }

            Console.WriteLine($"  {table.Name,-40} {count,8:N0} rows  {fields.Length,3} cols");
            return count;
        }

        /// <summary>
        /// Render one field value for TSV, flattening arrays and stripping the separators.
        /// </summary>
        private static string Cell(object value)
        {
            if (value == null)
                return "";

            if (value is string s)
                return Clean(s);

            if (value is System.Collections.IEnumerable list and not string)
                return string.Join(',', list.Cast<object>().Select(v => v?.ToString() ?? ""));

            return Clean(value.ToString());
        }

        private static async Task<int> Inspect(string tablePath, string tableName, string id,
            string filterField = null, string filterValue = null)
        {
            PropertyInfo property = typeof(GameTableManager)
                .GetProperties()
                .FirstOrDefault(p => p.Name.Equals(tableName, StringComparison.OrdinalIgnoreCase)
                    && p.PropertyType.IsGenericType
                    && p.PropertyType.GetGenericTypeDefinition() == typeof(GameTable<>));

            if (property == null)
            {
                Console.Error.WriteLine($"no game table called {tableName}");
                return 1;
            }

            Type entryType = property.PropertyType.GetGenericArguments().Single();

            // loaded straight from the file rather than through GameTableManager, because the manager takes the file
            // name from the [GameData] attribute and a table the server never reads does not carry one - Challenge
            // being exactly such a table. Going through the manager makes those tables uninspectable, which is
            // backwards: an unread table is the one you most need to look at.
            string filePath = Path.Combine(tablePath, property.Name + ".tbl");
            if (!File.Exists(filePath))
            {
                Console.Error.WriteLine($"no file at {filePath}");
                return 1;
            }

            object table = GameTableFactory.LoadGameTable(entryType, filePath);
            await Task.CompletedTask;

            var entries = (System.Collections.IEnumerable)table.GetType().GetProperty("Entries")!.GetValue(table)!;
            FieldInfo[] fields = entryType.GetFields();
            FieldInfo idField = fields.FirstOrDefault(f => f.Name == "Id");
            int matched = 0;

            foreach (object entry in entries)
            {
                if (entry == null)
                    continue;

                if (id != null && idField != null && Convert.ToString(idField.GetValue(entry)) != id)
                    continue;

                if (filterField != null)
                {
                    FieldInfo f = fields.FirstOrDefault(x =>
                        string.Equals(x.Name, filterField, StringComparison.OrdinalIgnoreCase));
                    if (f == null)
                    {
                        Console.Error.WriteLine($"no field '{filterField}' on {tableName}. fields: "
                            + string.Join(", ", fields.Select(x => x.Name)));
                        return 1;
                    }

                    if (Convert.ToString(f.GetValue(entry)) != filterValue)
                        continue;

                    matched++;
                }

                foreach (FieldInfo field in fields)
                {
                    object value = field.GetValue(entry);
                    if (value is Array array)
                        value = "[" + string.Join(",", array.Cast<object>()) + "]";

                    Console.WriteLine($"{field.Name}\t{value}");
                }

                Console.WriteLine();

                if (id != null)
                    return 0;
            }

            if (id != null)
                Console.Error.WriteLine($"no row {id} in {tableName}");

            // say so rather than exiting silently: an empty result and a wrong field name look identical
            // from the outside, and one of them is a typo you would spend ten minutes not noticing
            if (filterField != null)
                Console.Error.WriteLine($"{matched} row(s) where {filterField} = {filterValue}");

            return 0;
        }

        /// <summary>
        /// Return the display name for a <see cref="Spell4Entry"/>.
        /// </summary>
        /// <remarks>
        /// A Spell4 row carries the tier; the name is on the base spell it belongs to.
        /// </remarks>
        private static string NameOfSpell(GameTableManager manager, TextTable text, Spell4Entry entry)
        {
            Spell4BaseEntry baseEntry = manager.Spell4Base?.GetEntry(entry.Spell4BaseIdBaseSpell);
            return baseEntry == null ? "" : text.GetEntry(baseEntry.LocalizedTextIdName);
        }

        private static void Write<T>(string path, string header, GameTable<T> table, Func<T, string> line) where T : class, new()
        {
            if (table == null)
            {
                Console.Error.WriteLine($"skipped {Path.GetFileName(path)} - the table did not load");
                return;
            }

            using var writer = new StreamWriter(path);
            writer.WriteLine(header);

            long written = 0;
            foreach (T entry in table.Entries)
            {
                if (entry == null)
                    continue;

                writer.WriteLine(line(entry));
                written++;
            }

            Console.WriteLine($"{Path.GetFileName(path)}: {written} rows");
        }

        /// <summary>
        /// Strip anything that would break the column layout.
        /// </summary>
        private static string Clean(string value)
        {
            return string.IsNullOrEmpty(value) ? "" : value.Replace('\t', ' ').Replace('\r', ' ').Replace('\n', ' ').Trim();
        }
    }
}
