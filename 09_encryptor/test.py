from math import gcd
from pwn import *
from Crypto.Cipher import ChaCha20
from Crypto.Util.number import bytes_to_long,long_to_bytes,inverse
f3 = open('SuspiciousFile.txt.Encrypted','rb').read()

#random 2 number: 1 key (32 bytes), 1 nonce(12 bytes)
#then use ChaCha20 to encrypt b'\x00'*64 and use this result xor with original flag

# (const)  N1 = bytes_to_long(b'\xa1\x82/\xba\xba"n\x90\xb9\x01\xfc\xa1\x80\x7f\x84\x85Np\xf2:\xf1\xc2\x93\xd5\xb8T\x15\xb1\xc2\x80v\x85.\xbed\x81N\'\xf8\xa8\x18\xc2\x190\xa4\x08\xcc\xfdAz\xd7\xb1\x01!\x84\xddUl\x16Tk1\xa3\xff\xb6\xc5]#^\xfb\x12W*\xe2\\\xe9\x85\xcd\xb3\xfd\x1d%\x88\x19\xdd\xe0B\xc9\x88XRS\xc8\x83\n\x17q\rM\xa0\xad\xef\tFR\xfb\n\x01yZ{\xbe\x9c\xd8\x06\x97%$\xea\xb55\x88\xe7\xd3kw\x18\x9f'[::-1])
N1 = bytes_to_long(b'\xa1\x82/\xba\xba"n\x90\xb9\x01\xfc\xa1\x80\x7f\x84\x85Np\xf2:\xf1\xc2\x93\xd5\xb8T\x15\xb1\xc2\x80v\x85.\xbed\x81N\'\xf8\xa8\x18\xc2\x190\xa4\x08\xcc\xfdAz\xd7\xb1\x01!\x84\xddUl\x16Tk1\xa3\xff\xb6\xc5]#^\xfb\x12W*\xe2\\\xe9\x85\xcd\xb3\xfd\x1d%\x88\x19\xdd\xe0B\xc9\x88XRS\xc8\x83\n\x17q\rM\xa0\xad\xef\tFR\xfb\n\x01yZ{\xbe\x9c\xd8\x06\x97%$\xea\xb55\x88\xe7\xd3kw\x18\x9f'[::-1])
#   N2 = publickey = p*q
N2 = bytes_to_long(bytes.fromhex('dc425c720400e05a92eeb68d0313c84a978cbcf47474cbd9635eb353af864ea46221546a0f4d09aaa0885113e31db53b565c169c3606a241b569912a9bf95c91afbc04528431fdcee6044781fbc8629b06f99a11b99c05836e47638bbd07a232c658129aeb094ddaf4c3ad34563ee926a87123bc669f71eb6097e77c188b9bc9'))
#   Number3 = pow(v6,0x10001,N1)
N3 = bytes_to_long(bytes.fromhex('8e678f043c0d8b8d3dff39b28ce9974ff7d4162473080b54eefaa6decb8827717c6b24edfff7063375b6588acf8eca35c2033ef8ebe721436de6f2f66569b03df8c5861a68e57118c9f854b2e62ca9871f7207fafa96aceba11ffd37b6c4dbf95b256184983bad407c7973e84b23cd22579dd25bf4c1a03734d1a7b0dfdcfd44'))
#   ciphertext = pow(KEY,d,N2)
ciphertext = bytes_to_long(bytes.fromhex('5a04e95cd0e9bf0c8cdda2cbb0f50e7db8c89af791b4e88fd657237c1be4e6599bc4c80fd81bdb007e43743020a245d5f87df1c23c4d129b659f90ece2a5c22df1b60273741bf3694dd809d2c485030afdc6268431b2287c597239a8e922eb31174efcae47ea47104bc901cea0abb2cc9ef974d974f135ab1f4899946428184c'))

p = bytes_to_long(b'\x9f\x0e\xc0\xa8\xcd\x96#\x95>-\xc5z\xf7\xac\x1fC\xc3\x08\x8b$\xc9\xa6\xc0\x08\xf5h\x82\xb6@o\x93\xd4\r\xbd4\xe9\xb6\x07\x13\x85\xbf8\x07\x11\xbc\xeb\x8a\xa5\xf4K\x10\x8e\xad\xc2\xb9\xea\x97~+N\xd2S~\xf2'[::-1])
q = bytes_to_long(b'\xc7\x06"\x04;G\xd2!\x05_u\xac"F".\xdf\xd6\x83\xb3\xb3e\xcb\n\xcb*hrP\xb9\x8dR\xb6\xe9\xc0\xf6Qdu*c\x1a\xceb\xdd\x12\x06p\x8eW\xbb/\x11k2\xae\x0eD\x95~@\xd8?\xd4'[::-1])
phi = (p-1)*(q-1)
e = 0x10001
d = pow(e,-1,phi)
n3 = bytes_to_long(b'wg\x8a\x95\xfe\x7f\x00\x00`\xfd`\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x10\x00\x00\x00\x00\x00\x00\x00\x18\x00\x00\x00\x00\x00\x00\x00\x00\x00\xba\x93\xfe\x7f\x00\x00\xfeb@\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00@<@\x00\x00\x00\x00\x00\xfcUa\x93\xfe\x7f\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\xf5b@\x00\x00\x00\x00\x00o\x8bh\x93\xfe\x7f\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00@<@\x00\x00\x00\x00\x00'[::-1])
print(long_to_bytes(pow(n3,0x10001,N1))[::-1])

res = long_to_bytes(pow(ciphertext,N3,N2))

cipher = ChaCha20.new(key = res[:32],nonce = res[36:48])
print(xor(f3,cipher.encrypt(b'\x00'*64)))
