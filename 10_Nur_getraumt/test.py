from pwn import *

f = open('Nur.img','rb').read()
flag = b'\x0c\x00\x1d\x1a\x7f\x17\x1cN\x02\x11(\x08\x10H\x05\x00\x00\x1a\x7f*\xf6\x17D2\x0f\xfc\x1a`,\x08\x10\x1c`\x02\x19A\x17\x11Z\x0e\x1d\x0e9\n\x04'
print(xor(flag,b"Hast du etwas Zeit f\x9fr mich?"))
print()