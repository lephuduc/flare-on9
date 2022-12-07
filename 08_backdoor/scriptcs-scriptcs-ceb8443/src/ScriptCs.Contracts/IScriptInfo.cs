﻿using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace ScriptCs.Contracts
{
    public interface IScriptInfo
    {
        string ScriptPath { get; set; }
        IList<string> LoadedScripts { get; }
    }
}
