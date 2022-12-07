﻿using System;
using System.Collections.Generic;
using System.IO;
using System.Linq;
using ScriptCs.Contracts;

namespace ScriptCs
{
    public class FilePreProcessor : IFilePreProcessor
    {
        private readonly ILog _logger;

        private readonly IEnumerable<ILineProcessor> _lineProcessors;
        private readonly IEnumerable<IDirectiveLineProcessor> _directiveLineProcessors; 

        private readonly IFileSystem _fileSystem;

        public FilePreProcessor(IFileSystem fileSystem, ILogProvider logProvider, IEnumerable<ILineProcessor> lineProcessors)
        {
            Guard.AgainstNullArgument("fileSystem", fileSystem);
            Guard.AgainstNullArgument("logProvider", logProvider);

            _fileSystem = fileSystem;
            _logger = logProvider.ForCurrentType();
            _lineProcessors = lineProcessors;
            _directiveLineProcessors = _lineProcessors.OfType<IDirectiveLineProcessor>();
        }

        public virtual FilePreProcessorResult ProcessFile(string path)
        {
            return Process(context => ParseFile(path, context));
        }

        public virtual FilePreProcessorResult ProcessScript(string script)
        {
            var scriptLines = _fileSystem.SplitLines(script).ToList();
            return Process(context => ParseScript(scriptLines, context));
        }

        protected virtual FilePreProcessorResult Process(Action<FileParserContext> parseAction)
        {
            Guard.AgainstNullArgument("parseAction", parseAction);

            var context = new FileParserContext();

            _logger.DebugFormat("Starting pre-processing");

            parseAction(context);

            var code = GenerateCode(context);

            _logger.DebugFormat("Pre-processing finished successfully");

            return new FilePreProcessorResult
            {
                Namespaces = context.Namespaces,
                LoadedScripts = context.LoadedScripts,
                References = context.References,
                Code = code,
                ScriptPath = context.ScriptPath
            };
        }

        protected virtual string GenerateCode(FileParserContext context)
        {
            Guard.AgainstNullArgument("context", context);
            return string.Join(_fileSystem.NewLine, context.BodyLines);
        }

        public virtual void ParseFile(string path, FileParserContext context)
        {
            Guard.AgainstNullArgument("path", path);
            Guard.AgainstNullArgument("context", context);

            var fullPath = _fileSystem.GetFullPath(path);
            var filename = Path.GetFileName(path);

            if (context.LoadedScripts.Contains(fullPath))
            {
                _logger.DebugFormat("Skipping {0} because it's already been loaded.", filename);
                return;
            }

            _logger.DebugFormat("Processing {0}...", filename);

            if (context.ScriptPath == null)
            {
                context.ScriptPath = fullPath;
            }
            else
            {
                // Add script to loaded collection before parsing to avoid loop.
                context.LoadedScripts.Add(fullPath);
            }

            var scriptLines = _fileSystem.ReadFileLines(fullPath).ToList();

            InsertLineDirective(fullPath, scriptLines);
            InDirectory(fullPath, () => ParseScript(scriptLines, context));
        }

        public virtual void ParseScript(List<string> scriptLines, FileParserContext context)
        {
            Guard.AgainstNullArgument("scriptLines", scriptLines);
            Guard.AgainstNullArgument("context", context);

            var codeIndex = scriptLines.FindIndex(IsNonDirectiveLine);

            for (var index = 0; index < scriptLines.Count; index++)
            {
                var line = scriptLines[index];
                var isBeforeCode = index < codeIndex || codeIndex < 0;

                var wasProcessed = _lineProcessors.Any(x => x.ProcessLine(this, context, line, isBeforeCode));
                if (!wasProcessed)
                {
                    context.BodyLines.Add(line);
                }
            }
        }

        protected virtual void InsertLineDirective(string path, List<string> fileLines)
        {
            Guard.AgainstNullArgument("fileLines", fileLines);

            var bodyIndex = fileLines.FindIndex(line => IsNonDirectiveLine(line) && !IsUsingLine(line));
            if (bodyIndex == -1)
            {
                return;
            }

            var directiveLine = string.Format("#line {0} \"{1}\"", bodyIndex + 1, path);
            fileLines.Insert(bodyIndex, directiveLine);
        }

        private void InDirectory(string path, Action action)
        {
            var oldCurrentDirectory = _fileSystem.CurrentDirectory;
            _fileSystem.CurrentDirectory = _fileSystem.GetWorkingDirectory(path);

            action();

            _fileSystem.CurrentDirectory = oldCurrentDirectory;
        }

        private bool IsNonDirectiveLine(string line)
        {
            line = line.Trim();
            if (line.StartsWith("//") || line.Equals(string.Empty))
                return false;

            return !_directiveLineProcessors.Any(lp => lp.Matches(line));
        }

        private static bool IsUsingLine(string line)
        {
            return line.TrimStart(' ').StartsWith("using ") && !line.Contains("{") && line.Contains(";");
        }
    }
}
