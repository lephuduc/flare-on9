using System;
using System.Collections.Generic;
using System.Linq;
using System.Reflection;
using System.Text;
using System.Threading.Tasks;
namespace TestDll
{
    class Program
    {
        static void Main(string[] args)
        {
            string dllFile = @"D:\CTF\Flareon9\06_alamode\HowDoesThisWork.dll";
            var assembly = Assembly.LoadFile(dllFile);
            var type = assembly.GetType("FlareOn.Flag");
            var obj = Activator.CreateInstance(type);
            var method = type.GetMethod("GetFlag");
            var result = method.Invoke(obj, new object[] {"something"});
            Console.WriteLine(result);
            Console.ReadLine();
        }
    }
}