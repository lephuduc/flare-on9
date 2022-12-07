from pwn import *
import arc4
d1 = b'\xe1`\xa1\x18\x93.\x96\xads\xbbJ\x92\xde\x18\n\xaaAt\xad\xc0\x1d\x9f?\x19\xff+\x02\xdb\xd1\xcd\x1a\x00'
pipe = b'KK9Kg~grKQ{verXy'
AuthFail = b'Vbc\x7fxe~mvc~xy7Qv~{rs\x00\x00\x00\x00'
CloseHandle =b'T{xdr_vys{r'
ConnectNP = b'TxyyrtcYvzrsG~gr'
CreateNamedPipe = b'TervcrYvzrsG~grV'
disconnectedNP = b'S~dtxyyrtcYvzrsG~gr'
Create_thread = b'TervcrC\x7fervs'
FlushFileBuffers = b'Q{bd\x7fQ~{rUbqqred'
getlastErr = b'Prc[vdcReexe'
get_processHeap =b'PrcGextrdd_rvg'
lstrcmpA = b'{dcetzgV'
ReadFile=b'ErvsQ~{r'
WriteFile = b'@e~crQ~{r'

d1 = b'>9Q\xfb\xa2\x11\xf7\xb9,'
d2 = b'U\x8b\xec\x83\xec \xeb\xfe\xe1`\xa1\x18\x93.\x96\xads\xbbJ\x92\xde\x18\n\xaaAt\xad\xc0\x1d\x9f?\x19\xff+\x02\xdb\xd1\xcd\x1a\x00'
arc = arc4.ARC4(d2[0:8])

print(arc.decrypt(d1))
key = b'MyV0ic3!\x00'
print(arc.decrypt(d2[8:]))

