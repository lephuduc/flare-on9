# post http://www.evil.flare-on.com/ {'data': {'flag': b'/B3EPupkU5y2GEHyayw/LP25gd6OdCVVYehe+HqnyhwkEZP2aCxijmJkBcb5FA=='}, 'json': None}
import base64
from tkinter import ARC
from pwn import *
import arc4
data = b'/B3EPupkU5y2GEHyayw/LP25gd6OdCVVYehe+HqnyhwkEZP2aCxijmJkBcb5FA=='
print(len(base64.b64decode(data)))
arc = arc4.ARC4(b'PyArmor_Pr0tecteth_My_K3y')
print(arc.decrypt(data))
