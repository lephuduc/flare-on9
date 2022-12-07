from email import message
from math import gcd
from pwn import *
from Crypto.Cipher import ChaCha20
from Crypto.Util.number import bytes_to_long,long_to_bytes,inverse
f = open('SuspiciousFile.txt.Encrypted','rb').read()
N2 = bytes_to_long(bytes.fromhex('dc425c720400e05a92eeb68d0313c84a978cbcf47474cbd9635eb353af864ea46221546a0f4d09aaa0885113e31db53b565c169c3606a241b569912a9bf95c91afbc04528431fdcee6044781fbc8629b06f99a11b99c05836e47638bbd07a232c658129aeb094ddaf4c3ad34563ee926a87123bc669f71eb6097e77c188b9bc9'))
ciphertext = bytes_to_long(bytes.fromhex('5a04e95cd0e9bf0c8cdda2cbb0f50e7db8c89af791b4e88fd657237c1be4e6599bc4c80fd81bdb007e43743020a245d5f87df1c23c4d129b659f90ece2a5c22df1b60273741bf3694dd809d2c485030afdc6268431b2287c597239a8e922eb31174efcae47ea47104bc901cea0abb2cc9ef974d974f135ab1f4899946428184c'))

e = 0x10001
m = long_to_bytes(pow(ciphertext,e,N2))[::-1]
print(m) 
cipher = ChaCha20.new(key = m[:32],nonce = m[36:48])
res = cipher.encrypt(b'\x00'*64)
print(xor(f,res))