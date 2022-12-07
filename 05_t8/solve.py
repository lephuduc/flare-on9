from base64 import b64decode,b64encode
from pwn import *
from hashlib import md5
from arc4 import ARC4
import requests

data1 = b'TdQdBRa1nxGU06dbB27E7SQ7TJ2+cd7zstLXRQcLbmh2nTvDm1p5IfT/Cu0JxShk6tHQBRWwPlo9zA1dISfslkLgGDs41WK12ibWIflqLE4Yq3OYIEnLNjwVHrjL2U4Lu3ms+HQc4nfMWXPgcOHb4fhokk93/AJd5GTuC5z+4YsmgRh1Z90yinLBKB+fmGUyagT6gon/KHmJdvAOQ8nAnl8K/0XG+8zYQbZRwgY6tHvvpfyn9OXCyuct5/cOi8KWgALvVHQWafrp8qB/JtT+t5zmnezQlp3zPL4sj2CJfcUTK5copbZCyHexVD4jJN+LezJEtrDXP1DJNg=='
data2 = b'F1KFlZbNGuKQxrTD/ORwudM8S8kKiL5F906YlR8TKd8XrKPeDYZ0HouiBamyQf9/Ns7u3C2UEMLoCA0B8EuZp1FpwnedVjPSdZFjkieYqWzKA7up+LYe9B4dmAUM2lYkmBSqPJYT6nEg27n3X656MMOxNIHt0HsOD0d+'

s1 = b64decode(data1)
s2 = b64decode(data2)


#send request to flare-on.com
#address = 0x...
# patch random number XXXXX   ;[patch_byte(address+2*i,j) for i,j in zip(range(5),b'11950')]
#start = 0x.....
# x1 = b'TdQdBRa1nxGU06dbB27E7SQ7TJ2+cd7zstLXRQcLbmh2nTvDm1p5IfT/Cu0JxShk6tHQBRWwPlo9zA1dISfslkLgGDs41WK12ibWIflqLE4Yq3OYIEnLNjwVHrjL2U4Lu3ms+HQc4nfMWXPgcOHb4fhokk93/AJd5GTuC5z+4YsmgRh1Z90yinLBKB+fmGUyagT6gon/KHmJdvAOQ8nAnl8K/0XG+8zYQbZRwgY6tHvvpfyn9OXCyuct5/cOi8KWgALvVHQWafrp8qB/JtT+t5zmnezQlp3zPL4sj2CJfcUTK5copbZCyHexVD4jJN+LezJEtrDXP1DJNg=='
# x2 = b'F1KFlZbNGuKQxrTD/ORwudM8S8kKiL5F906YlR8TKd8XrKPeDYZ0HouiBamyQf9/Ns7u3C2UEMLoCA0B8EuZp1FpwnedVjPSdZFjkieYqWzKA7up+LYe9B4dmAUM2lYkmBSqPJYT6nEg27n3X656MMOxNIHt0HsOD0d+'

#clear bytes: [patch_byte(start+i,0) for i in range(0x34b)]
#change bytes base64: [patch_byte(start+i,j) for i,j in zip(range(len(x)),x) ]


# key = md5(b'F\x00O\x009\x001\x009\x007\x009\x002\x00')
# arc = ARC4(key)
# decrypted = arc.decrypt(b"a\x00h\x00o\x00y\x00")
# data_to_send = b64decode(decrypted) (zero extended)
#1: recv data, b64decode, rc4 decrypt(key)
#2: split by ','

#11950    b'F\x00O\x009\x001\x001\x009\x005\x000\x00'
key1 = md5(b'F\x00O\x009\x001\x001\x009\x005\x000\x00')

key1 = b''.join([(i+'\x00').encode() for i in key1.digest().hex()])
arc = ARC4(key1)
decrypt1 = arc.decrypt(s1)
print(decrypt1)

# r = requests.post(url = 'http://flare-on.com',data='y\x00d\x00N\x008\x00B\x00X\x00q\x001\x006\x00R\x00E\x00=\x00')
# print(r.text)