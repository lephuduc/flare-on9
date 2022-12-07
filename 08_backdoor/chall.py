# from flag import flag #this is secret
import os 


def xor(s1,s2): # xor 2 string
	if len(s2)>len(s1):
		return xor(s2,s1)
	s2=s2*(1+len(s1)//len(s2))
	return bytes(x^y for x,y in zip(s1,s2))

key=os.urandom(1)
# ciphertext=xor(flag,key)

# print(f"ciphertext: {ciphertext}")


ciphertext=b'\xd1\xb7\xfd\xfe\xe9\xf4\xd9\xf5\xf2\xe7\xf4\xf2\xe3\xf4\xd9\xe7\xd8\xe4\xbb\xe5\xab\xb8\xe4\xbb\xe7\xd8\xe5\xa7\xa7\xa7\xfb'

from pwn import *
print(xor(ciphertext,0x86))