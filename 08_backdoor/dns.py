import math
import base64
from telnetlib import DO

CharsDomain = "abcdefghijklmnopqrstuvwxyz0123456789"
CharsCounter = "amsjl6zci20dbt35guhw7n1fqvx4k8y9rpoe"

class RandomMersenneTwister():
    def __init__(self, c_seed=5489):

        (self.w, self.n, self.m, self.r) = (32, 624, 397, 31)
        self.a = 0x9908B0DF
        (self.u, self.d) = (11, 0xFFFFFFFF)
        (self.s, self.b) = (7, 0x9D2C5680)
        (self.t, self.c) = (15, 0xEFC60000)
        self.l = 18
        self.f = 1812433253

        self.MT = [0 for i in range(self.n)]
        self.index = self.n+1
        self.lower_mask = 0x7FFFFFFF
        self.upper_mask = 0x80000000

        self.c_seed = c_seed
        self.seed(c_seed)
    def seed(self, num):

        self.MT[0] = num
        self.index = self.n
        for i in range(1, self.n):
            temp = self.f * (self.MT[i-1] ^ (self.MT[i-1] >> (self.w-2))) + i
            self.MT[i] = temp & 0xffffffff

    def twist(self):

        for i in range(0, self.n):
            x = (self.MT[i] & self.upper_mask) + \
                (self.MT[(i+1) % self.n] & self.lower_mask)
            xA = x >> 1
            if (x % 2) != 0:
                xA = xA ^ self.a
            self.MT[i] = self.MT[(i + self.m) % self.n] ^ xA
        self.index = 0

    def extract_number(self):
     
        if self.index >= self.n:
            self.twist()

        y = self.MT[self.index]
        y = y ^ ((y >> self.u) & self.d)
        y = y ^ ((y << self.s) & self.b)
        y = y ^ ((y << self.t) & self.c)
        y = y ^ (y >> self.l)

        self.index += 1
        return y & 0xffffffff

    def GetRandomRange(self , minn , maxx):
        num = maxx - minn
        randnum = self.extract_number()
        return minn + (randnum % num)
def ConvertIntToDomain(value):
    text = ""
    length = len(CharsDomain)
    while 1:
        text = CharsDomain[value % length] + text 
        value //= length
        if value <= 0:
            break

    return text    
def PadLeft(text,totalWidth,paddingChar):
    if totalWidth < len(text):
        return text
    return paddingChar*(totalWidth-len(text)) + text
def ConvertIntToCounter(value):
    text = ""
    length = len(CharsCounter)
    while 1:
        text = CharsCounter[value % length] + text 
        value //= length
        if value <= 0:
            break

    return text
def MapBaseSubdomainCharacters( data,  shuffle):
       text = ""
       for i in range(len(data)):
            text += shuffle[CharsDomain.index(data[i])];
       return text     
def Shuffle(seed):
    CharsDomain = "abcdefghijklmnopqrstuvwxyz0123456789"
    randomMersenneTwister = RandomMersenneTwister(seed)
    length = len(CharsDomain)
    text2 = ""
    for i in range(length):
                    randomRange = randomMersenneTwister.GetRandomRange(0,len(CharsDomain))
                    text2 += CharsDomain[randomRange];
                    CharsDomain = CharsDomain.replace(CharsDomain[randomRange],'')
                
    return text2
for seed in range(46656):
    FirstAliveKey = "flareon"
    shuffle  = Shuffle(seed)
    domain = ConvertIntToDomain(0) + FirstAliveKey
    Domain = MapBaseSubdomainCharacters(domain, shuffle) + PadLeft(ConvertIntToCounter(seed),3,CharsCounter[0]) + "."
    print(Domain)