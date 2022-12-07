﻿using System;
using ScriptCs.Contracts;

namespace ScriptCs
{
    public class DebugScriptExecutor : ScriptExecutor
    {
        public DebugScriptExecutor(IFileSystem fileSystem, IFilePreProcessor filePreProcessor, IScriptEngine scriptEngine, ILogProvider logProvider, IScriptLibraryComposer composer, IScriptInfo scriptInfo)
            : base(fileSystem, filePreProcessor, scriptEngine, logProvider, composer, scriptInfo)
        {
        }
    }
}
