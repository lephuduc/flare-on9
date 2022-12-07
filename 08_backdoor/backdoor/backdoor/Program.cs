// See https://aka.ms/new-console-template for more information
using AsmResolver.PE.File;
using AsmResolver.DotNet;
using System.Reflection.Emit;
using AsmResolver;
using AsmResolver.PE.File.Headers;
using AsmResolver.PE.DotNet.Cil;  
using AsmResolver.DotNet.Code.Cil;
using System.Security.Cryptography;
using System.Reflection;
using System.Text;
using System.Diagnostics;

class backdoor
{
    public static object flare_71(InvalidProgramException e, object[] args, Dictionary<uint, int> m, byte[] b)
    {
        StackTrace stackTrace = new StackTrace();
        int metadataToken = stackTrace.GetFrame(0).GetMethod().MetadataToken;
           Console.WriteLine(stackTrace.GetFrame(0).GetMethod().ToString());
        Module module = typeof(backdoor).Module;
        MethodInfo methodInfo = (MethodInfo)module.ResolveMethod(metadataToken);
        MethodBase methodBase = module.ResolveMethod(metadataToken);
        ParameterInfo[] parameters = methodInfo.GetParameters();
        Type[] array = new Type[parameters.Length];
        SignatureHelper localVarSigHelper = SignatureHelper.GetLocalVarSigHelper();
        for (int i = 0; i < array.Length; i++)
        {
            array[i] = parameters[i].ParameterType;
        }
        Type declaringType = methodBase.DeclaringType;
        DynamicMethod dynamicMethod = new DynamicMethod("", methodInfo.ReturnType, array, declaringType, true);
        DynamicILInfo dynamicILInfo = dynamicMethod.GetDynamicILInfo();
        MethodBody methodBody = methodInfo.GetMethodBody();
        foreach (LocalVariableInfo localVariableInfo in methodBody.LocalVariables)
        {
            localVarSigHelper.AddArgument(localVariableInfo.LocalType);
        }
        byte[] signature = localVarSigHelper.GetSignature();
        dynamicILInfo.SetLocalSignature(signature);
        foreach (KeyValuePair<uint, int> keyValuePair in m)
        {
            int value = keyValuePair.Value;
            uint key = keyValuePair.Key;
            bool flag = value >= 1879048192 && value < 1879113727;
            int tokenFor;
            if (flag)
            {
                tokenFor = dynamicILInfo.GetTokenFor(module.ResolveString(value));
            }
            else
            {
                MemberInfo memberInfo = declaringType.Module.ResolveMember(value, null, null);
                bool flag2 = memberInfo.GetType().Name == "RtFieldInfo";
                if (flag2)
                {
                    tokenFor = dynamicILInfo.GetTokenFor(((FieldInfo)memberInfo).FieldHandle, ((TypeInfo)((FieldInfo)memberInfo).DeclaringType).TypeHandle);
                }
                else
                {
                    bool flag3 = memberInfo.GetType().Name == "RuntimeType";
                    if (flag3)
                    {
                        tokenFor = dynamicILInfo.GetTokenFor(((TypeInfo)memberInfo).TypeHandle);
                    }
                    else
                    {
                        bool flag4 = memberInfo.Name == ".ctor" || memberInfo.Name == ".cctor";
                        if (flag4)
                        {
                            tokenFor = dynamicILInfo.GetTokenFor(((ConstructorInfo)memberInfo).MethodHandle, ((TypeInfo)((ConstructorInfo)memberInfo).DeclaringType).TypeHandle);
                        }
                        else
                        {
                            tokenFor = dynamicILInfo.GetTokenFor(((MethodInfo)memberInfo).MethodHandle, ((TypeInfo)((MethodInfo)memberInfo).DeclaringType).TypeHandle);
                        }
                    }
                }
            }
            b[(int)key] = (byte)tokenFor;
            b[(int)(key + 1U)] = (byte)(tokenFor >> 8);
            b[(int)(key + 2U)] = (byte)(tokenFor >> 16);
            b[(int)(key + 3U)] = (byte)(tokenFor >> 24);
        }
        dynamicILInfo.SetCode(b, methodBody.MaxStackSize);
        return dynamicMethod.Invoke(null, args);
    }
    public static byte[] RC4(byte[] bytes, byte[] key)
    {
        byte[] z = new byte[bytes.Length];
        byte[] s = new byte[256];
        byte[] k = new byte[256];
        byte temp;
        int i, j;

        for (i = 0; i < 256; i++)
        {
            s[i] = (byte)i;
            k[i] = key[i % key.GetLength(0)];
        }

        j = 0;
        for (i = 0; i < 256; i++)
        {
            j = (j + s[i] + k[i]) % 256;
            temp = s[i];
            s[i] = s[j];
            s[j] = temp;
        }

        i = j = 0;
        for (int x = 0; x < z.GetLength(0); x++)
        {
            i = (i + 1) % 256;
            j = (j + s[i]) % 256;
            temp = s[i];
            s[i] = s[j];
            s[j] = temp;
            int t = (s[i] + s[j]) % 256;
            z[x] = (byte)(bytes[x] ^ s[t]);
        }
        return z;
    }
    public static void printbyte(byte[] b)
    {
        for (var i = 0; i < b.Length; i++)
        {
            var x = b[i].ToString("X");
            if (x.Length < 2)
            {
                x = "0" + x;
            }
            Console.Write(x);
        }
    }
    public static byte[] strip(byte[] b)
    {
        while (b[b.Length - 1] == 0)
        {
            b = b.SkipLast(1).ToArray();
        }
        return b;
    }
    public static void Main(String[] args)
    {
        byte[] key = { 0x12, 0x78, 0xAB, 0xDF };
        var peFile = PEFile.FromFile(@"D:\CTF\Flareon9\08_backdoor\FlareOn.Backdoor.exe");
        
        foreach (var section in peFile.Sections)
        {
            byte[] encrypted = section.ToArray();
            //delete last bytes 00
           encrypted = strip(encrypted);
            //byte[] bytes = RC4(encrypted, key);
            Dictionary<uint, int> m = new Dictionary<uint, int> {};

            flare_71(null, new object[] {null,null},  m, encrypted);
            if (encrypted.Length>= 0x33 - 4 && encrypted.Length<= 0x33 + 4)
            {
                Console.WriteLine(section.Offset.ToString("X")+" - " + encrypted.Length);
            }
               
        }
    }
}