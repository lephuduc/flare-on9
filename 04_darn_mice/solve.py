import subprocess
from Crypto.Protocol.KDF import PBKDF2
from Crypto.Hash import SHA256
from Crypto.Util.Padding import unpad
from Crypto.Cipher import AES
v5 = [0]*35
v5[0] = ord('P')
v5[1] = ord('^')
v5[2] = ord('^')
v5[3] = 0xA3
v5[4] = 0x4F
v5[5] = 0x5B
v5[6] = 0x51
v5[7] = 0x5E
v5[8] = 0x5E
v5[9] = 0x97
v5[10] = 0xA3
v5[11] = 128
v5[12] = 0x90
v5[13] = 0xA3
v5[14] = 128
v5[15] = 0x90
v5[16] = 0xA3
v5[17] = 128
v5[18] = 0x90
v5[19] = 0xA3
v5[20] = 128
v5[21] = 0x90
v5[22] = 0xA3
v5[23] = 128
v5[24] = 0x90
v5[25] = 0xA3
v5[26] = 128
v5[27] = 0x90
v5[28] = 0xA3
v5[29] = 128
v5[30] = 0x90
v5[31] = 0xA2
v5[32] = 0xA3
v5[33] = 0x6B
v5[34] = 0x7F
salt = b'salty'
pw =''
for i in v5:
    pw+=chr(0xc3-i)
pw = pw.encode()
print(pw)

ciphertext = b'\x7f7q@#\x98\x93\xd4\x00Q\xbfN\x04c\x0b\xb1\xe3\xbch\x14\xf6v\xb66u\x8e\x86Mj\xb4\x07\x93,\xb2\xe1\xd0\x16\xdf\xbc\xfd\xc7\xf5s-Y\x00\x00\x00'

pbkdf2Hash = PBKDF2(pw, salt, 32 + 16)
key = pbkdf2Hash[0:32]
iv = pbkdf2Hash[32:32 + 16]

cipher = AES.new(key, AES.MODE_CBC, iv)
decrypted = cipher.decrypt(ciphertext)

print(decrypted)
