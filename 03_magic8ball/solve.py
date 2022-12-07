import arc4
byte = [0]*10
byte[0] = 0x33122A35
byte[1] = 0xB2645787
byte[2] = 0x34A6EF00
byte[3] = 0x3EDEE001
byte[4] = 0x40EC2101
byte[5] = 0xB0691D26
byte[6] = 0x7BB269B0
byte[7] = 0x6EB2256
byte[8] = 0xCB5DF2BE
byte[9] = 0x512B0F79
for i in range(10):
    byte[i]=byte[i].to_bytes(4,'little')
byte = b''.join(byte)
cipher = arc4.ARC4(b"LLURULDUL")
text = cipher.decrypt(byte)
print(text)