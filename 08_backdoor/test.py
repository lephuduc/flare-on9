from email.mime import base
import arc4

dic = {
    88:0,214:0,215:0,95:0,65024:0,59:3,46:2,60:3,47:2,65:3,52:2,61:3,48:2,66:3,53:2,62:3,49:2,67:3,54:2,63:3,50:2,68:3,55:2,64:3,51:2,140:1,56:3,43:2,1:0,57:3,44:2,58:3,45:2,40:1,41:1,111:1,116:1,65025:0,65026:0,65027:0,195:0,65028:0,65029:0,65046:1,211:0,103:0,104:0,105:0,106:0,212:0,138:0,179:0,130:0,181:0,131:0,183:0,132:0,185:0,133:0,213:0,139:0,180:0,134:0,182:0,135:0,184:0,136:0,186:0,137:0,118:0,107:0,108:0,224:0,210:0,209:0,109:0,110:0,65047:0,112:1,91:0,92:0,37:0,65041:0,220:0,65048:0,65045:1,117:1,39:1,65033:5,2:0,3:0,4:0,5:0,14:4,65034:5,15:4,32:6,22:0,23:0,24:0,25:0,26:0,27:0,28:0,29:0,30:0,21:0,31:4,33:7,34:6,35:7,163:1,151:0,144:0,146:0,148:0,150:0,152:0,153:0,154:0,145:0,147:0,149:0,143:1,123:1,124:1,65030:1,77:0,70:0,72:0,74:0,76:0,78:0,79:0,80:0,71:0,73:0,75:0,142:0,65036:5,6:0,7:0,8:0,9:0,17:4,65037:5,18:4,20:0,113:1,126:1,127:1,114:1,208:1,65031:1,221:3,222:2,65039:0,198:1,90:0,216:0,217:0,101:0,141:1,115:1,65049:4,0:0,102:0,96:0,38:0,254:0,253:0,252:0,251:0,250:0,249:0,248:0,255:0,65054:0,65053:0,194:1,93:0,94:0,42:0,65050:0,98:0,99:0,100:0,65052:1,65035:5,16:4,164:1,155:0,156:0,157:0,158:0,159:0,160:0,161:0,162:0,125:1,223:0,82:0,83:0,84:0,85:0,86:0,87:0,81:0,65038:5,10:0,11:0,12:0,13:0,19:4,129:1,128:1,89:0,218:0,219:0,69:8,65044:0,122:0,65042:4,121:1,165:1,65043:0,97:0
    }
def flared_68(b,o):
    num = b[o + 3] * 16777216
    num += b[o + 2] * 65536
    num += b[o + 1] * 256
    return num + b[o]
def get_bytes(address,length):
    f = open('FlareOn.Backdoor.exe','rb').read()
    print(f[address:address+length])
    arc = arc4.ARC4( bytes([0x12, 0x78, 0xAB, 0xDF]))
    b = list(arc.decrypt(f[address:address+length]))
    print(bytes(b))
    j = 0
    while (j < len(b)):
        key = 0
        if (b[j] == 254):
            key = 65024 + b[j + 1]
            j+=1
        else:
            key = b[j]
        j+=1
        match (dic[key]):
            case 1:
                num =flared_68(b, j)
                num ^= 2727913149
                b[j] = num&0xff
                b[j + 1] = (num >> 8)&0xff
                b[j + 2] = (num >> 16)&0xff
                b[j + 3] = (num >> 24)&0xff
                j += 4
                continue
            case 2:
                j+=1
                continue
            case 4:
                j+=1
                continue
            case 3:
                j += 4
                continue
            case 6:
                j += 4
                continue
            case 5:
                j += 2
                continue
            case 7:
                j += 8
                continue
            case 8:
                j += 4 + flared_68(b, j) * 4
                continue
    return bytes(b)
# print(bytes([0x00, 0x17, 0x72, 0x02, 0x00, 0x00, 0x70, 0x12, 0x00, 0x73, 0x03, 0x00, 0x00, 0x06, 0x0B, 0x00, 0x06, 0x0C, 0x08, 0x39, 0xD1, 0x00, 0x00, 0x00, 0x00, 0x73, 0x04, 0x00, 0x00, 0x06, 0x0D, 0x28, 0x05, 0x00, 0x00, 0x06, 0x00, 0x28, 0x06, 0x00, 0x00, 0x06, 0x00, 0x38, 0xB4, 0x00, 0x00, 0x00, 0x00, 0x00, 0x28, 0x07, 0x00, 0x00, 0x06, 0x13, 0x05, 0x11, 0x05, 0x13, 0x04, 0x11, 0x04, 0x45, 0x08, 0x00, 0x00, 0x00, 0x02, 0x00, 0x00, 0x00, 0x0B, 0x00, 0x00, 0x00, 0x18, 0x00, 0x00, 0x00, 0x25, 0x00, 0x00, 0x00, 0x32, 0x00, 0x00, 0x00, 0x3F, 0x00, 0x00, 0x00, 0x4C, 0x00, 0x00, 0x00, 0x59, 0x00, 0x00, 0x00, 0x2B, 0x64, 0x16, 0x28, 0x08, 0x00, 0x00, 0x06, 0x26, 0x2B, 0x5B, 0x28, 0x09, 0x00, 0x00, 0x06, 0x28, 0x0A, 0x00, 0x00, 0x06, 0x26, 0x2B, 0x4E, 0x28, 0x0B, 0x00, 0x00, 0x06, 0x28, 0x0C, 0x00, 0x00, 0x06, 0x26, 0x2B, 0x41, 0x28, 0x0D, 0x00, 0x00, 0x06, 0x28, 0x0E, 0x00, 0x00, 0x06, 0x26, 0x2B, 0x34, 0x28, 0x0F, 0x00, 0x00, 0x06, 0x28, 0x10, 0x00, 0x00, 0x06, 0x26, 0x2B, 0x27, 0x28, 0x11, 0x00, 0x00, 0x06, 0x28, 0x12, 0x00, 0x00, 0x06, 0x26, 0x2B, 0x1A, 0x28, 0x13, 0x00, 0x00, 0x06, 0x28, 0x14, 0x00, 0x00, 0x06, 0x26, 0x2B, 0x0D, 0x28, 0x15, 0x00, 0x00, 0x06, 0x28, 0x16, 0x00, 0x00, 0x06, 0x26, 0x2B, 0x00, 0x00, 0xDE, 0x0F, 0x13, 0x06, 0x00, 0x00, 0x00, 0xDE, 0x05, 0x26, 0x00, 0x00, 0xDE, 0x00, 0x00, 0xDE, 0x00, 0x17, 0x28, 0x17, 0x00, 0x00, 0x06, 0x00, 0x00, 0x38, 0x47, 0xFF, 0xFF, 0xFF, 0x00, 0xDE, 0x0B, 0x07, 0x2C, 0x07, 0x07, 0x6F, 0x18, 0x00, 0x00, 0x06, 0x00, 0xDC, 0x2A]))
# get_bytes(0x00b0b000,0xf8)
import base64
d = [
    b'RwBlAHQALQBEAG4AcwBDAGwAaQBlAG4AdABTAGUAcgB2AGUAcgBBAGQAZAByAGUAcwBzACAALQBBAGQAZAByAGUAcwBzAEYAYQBtAGkAbAB5ACAASQBQAHYANAAgAHwAIABTAGUAbABlAGMAdAAtAE8AYgBqAGUAYwB0ACAAUwBFAFIAVgBFAFIAQQBkAGQAcgBlAHMAcwBlAHMA=',
    b'JChwaW5nIC1uIDEgMTAuNjUuNDUuMyB8IGZpbmRzdHIgL2kgdHRsKSAtZXEgJG51bGw7JChwaW5nIC1uIDEgMTAuNjUuNC41MiB8IGZpbmRzdHIgL2kgdHRsKSAtZXEgJG51bGw7JChwaW5nIC1uIDEgMTAuNjUuMzEuMTU1IHwgZmluZHN0ciAvaSB0dGwpIC1lcSAkbnVsbDskKHBpbmcgLW4gMSBmbGFyZS1vbi5jb20gfCBmaW5kc3RyIC9pIHR0bCkgLWVxICRudWxs',
    # b'JAAoAHAAaQBuAGcAIAAtAG4AIAAxACAAMQAwAC4AMQAwAC4AMgAyAC4ANAAyACAAfAAgAGYAaQBuAGQAcwB0AHIAIAAvAGkAIAB0AHQAbAApACAALQBlAHEAIAAkAG4AdQBsAGwAOwAkACgAcABpAG4AZwAgAC0AbgAgADEAIAAxADAALgAxADAALgAyADMALgAyADAAMAAgAHwAIABmAGkAbgBkAHMAdAByACAALwBpACAAdAB0AGwAKQAgAC0AZQBxACAAJABuAHUAbABsADsAJAAoAHAAaQBuAGcAIAAtAG4AIAAxACAAMQAwAC4AMQAwAC4ANAA1AC4AMQA5ACAAfAAgAGYAaQBuAGQAcwB0AHIAIAAvAGkAIAB0AHQAbAApACAALQBlAHEAIAAkAG4AdQBsAGwAOwAkACgAcABpAG4AZwAgAC0AbgAgADEAIAAxADAALgAxADAALgAxADkALgA1ADAAIAB8ACAAZgBpAG4AZABzAHQAcgAgAC8AaQAgAHQAdABsACkAIAAtAGUAcQAgACQAbgB1AGwAbAA'
    b'JAAoAHAAaQBuAGcAIAAtAG4AIAAxACAAMQAwAC4ANgA1AC4ANQAxAC4AMQAxACAAfAAgAGYAaQBuAGQAcwB0AHIAIAAvAGkAIAB0AHQAbAApACAALQBlAHEAIAAkAG4AdQBsAGwAOwAkACgAcABpAG4AZwAgAC0AbgAgADEAIAAxADAALgA2ADUALgA2AC4AMQAgAHwAIABmAGkAbgBkAHMAdAByACAALwBpACAAdAB0AGwAKQAgAC0AZQBxACAAJABuAHUAbABsADsAJAAoAHAAaQBuAGcAIAAtAG4AIAAxACAAMQAwAC4ANgA1AC4ANQAyAC4AMgAwADAAIAB8ACAAZgBpAG4AZABzAHQAcgAgAC8AaQAgAHQAdABsACkAIAAtAGUAcQAgACQAbgB1AGwAbAA7ACQAKABwAGkAbgBnACAALQBuACAAMQAgADEAMAAuADYANQAuADYALgAzACAAfAAgAGYAaQBuAGQAcwB0AHIAIAAvAGkAIAB0AHQAbAApACAALQBlAHEAIAAkAG4AdQBsAGwA',
    b'JAAoAHAAaQBuAGcAIAAtAG4AIAAxACAAMQAwAC4AMQAwAC4AMQAwAC4ANAAgAHwAIABmAGkAbgBkAHMAdAByACAALwBpACAAdAB0AGwAKQAgAC0AZQBxACAAJABuAHUAbABsADsAJAAoAHAAaQBuAGcAIAAtAG4AIAAxACAAMQAwAC4AMQAwAC4ANQAwAC4AMQAwACAAfAAgAGYAaQBuAGQAcwB0AHIAIAAvAGkAIAB0AHQAbAApACAALQBlAHEAIAAkAG4AdQBsAGwAOwAkACgAcABpAG4AZwAgAC0AbgAgADEAIAAxADAALgAxADAALgAyADIALgA1ADAAIAB8ACAAZgBpAG4AZABzAHQAcgAgAC8AaQAgAHQAdABsACkAIAAtAGUAcQAgACQAbgB1AGwAbAA7ACQAKABwAGkAbgBnACAALQBuACAAMQAgADEAMAAuADEAMAAuADQANQAuADEAOQAgAHwAIABmAGkAbgBkAHMAdAByACAALwBpACAAdAB0AGwAKQAgAC0AZQBxACAAJABuAHUAbABsAA==',
    b'JAAoAHAAaQBuAGcAIAAtAG4AIAAxACAAMQAwAC4AMQAwAC4AMgAxAC4AMgAwADEAIAB8ACAAZgBpAG4AZABzAHQAcgAgAC8AaQAgAHQAdABsACkAIAAtAGUAcQAgACQAbgB1AGwAbAA7ACQAKABwAGkAbgBnACAALQBuACAAMQAgADEAMAAuADEAMAAuADEAOQAuADIAMAAxACAAfAAgAGYAaQBuAGQAcwB0AHIAIAAvAGkAIAB0AHQAbAApACAALQBlAHEAIAAkAG4AdQBsAGwAOwAkACgAcABpAG4AZwAgAC0AbgAgADEAIAAxADAALgAxADAALgAxADkALgAyADAAMgAgAHwAIABmAGkAbgBkAHMAdAByACAALwBpACAAdAB0AGwAKQAgAC0AZQBxACAAJABuAHUAbABsADsAJAAoAHAAaQBuAGcAIAAtAG4AIAAxACAAMQAwAC4AMQAwAC4AMgA0AC4AMgAwADAAIAB8ACAAZgBpAG4AZABzAHQAcgAgAC8AaQAgAHQAdABsACkAIAAtAGUAcQAgACQAbgB1AGwAbAA=',
    b'JAAoAHAAaQBuAGcAIAAtAG4AIAAxACAAMQAwAC4ANgA1AC4ANAA1AC4AMQA4ACAAfAAgAGYAaQBuAGQAcwB0AHIAIAAvAGkAIAB0AHQAbAApACAALQBlAHEAIAAkAG4AdQBsAGwAOwAkACgAcABpAG4AZwAgAC0AbgAgADEAIAAxADAALgA2ADUALgAyADgALgA0ADEAIAB8ACAAZgBpAG4AZABzAHQAcgAgAC8AaQAgAHQAdABsACkAIAAtAGUAcQAgACQAbgB1AGwAbAA7ACQAKABwAGkAbgBnACAALQBuACAAMQAgADEAMAAuADYANQAuADMANgAuADEAMwAgAHwAIABmAGkAbgBkAHMAdAByACAALwBpACAAdAB0AGwAKQAgAC0AZQBxACAAJABuAHUAbABsADsAJAAoAHAAaQBuAGcAIAAtAG4AIAAxACAAMQAwAC4ANgA1AC4ANQAxAC4AMQAwACAAfAAgAGYAaQBuAGQAcwB0AHIAIAAvAGkAIAB0AHQAbAApACAALQBlAHEAIAAkAG4AdQBsAGwA',
    b'bnNsb29rdXAgZmxhcmUtb24uY29tIHwgZmluZHN0ciAvaSBBZGRyZXNzO25zbG9va3VwIHdlYm1haWwuZmxhcmUtb24uY29tIHwgZmluZHN0ciAvaSBBZGRyZXNz',
    b'JAAoAHAAaQBuAGcAIAAtAG4AIAAxACAAMQAwAC4ANgA1AC4ANAAuADUAMAAgAHwAIABmAGkAbgBkAHMAdAByACAALwBpACAAdAB0AGwAKQAgAC0AZQBxACAAJABuAHUAbABsADsAJAAoAHAAaQBuAGcAIAAtAG4AIAAxACAAMQAwAC4ANgA1AC4ANAAuADUAMQAgAHwAIABmAGkAbgBkAHMAdAByACAALwBpACAAdAB0AGwAKQAgAC0AZQBxACAAJABuAHUAbABsADsAJAAoAHAAaQBuAGcAIAAtAG4AIAAxACAAMQAwAC4ANgA1AC4ANgA1AC4ANgA1ACAAfAAgAGYAaQBuAGQAcwB0AHIAIAAvAGkAIAB0AHQAbAApACAALQBlAHEAIAAkAG4AdQBsAGwAOwAkACgAcABpAG4AZwAgAC0AbgAgADEAIAAxADAALgA2ADUALgA1ADMALgA1ADMAIAB8ACAAZgBpAG4AZABzAHQAcgAgAC8AaQAgAHQAdABsACkAIAAtAGUAcQAgACQAbgB1AGwAbAA7ACQAKABwAGkAbgBnACAALQBuACAAMQAgADEAMAAuADYANQAuADIAMQAuADIAMAAwACAAfAAgAGYAaQBuAGQAcwB0AHIAIAAvAGkAIAB0AHQAbAApACAALQBlAHEAIAAkAG4AdQBsAGwA',
    b'RwBlAHQALQBOAGUAdABUAEMAUABDAG8AbgBuAGUAYwB0AGkAbwBuACAAfAAgAFcAaABlAHIAZQAtAE8AYgBqAGUAYwB0ACAAewAkAF8ALgBTAHQAYQB0AGUAIAAtAGUAcQAgACIARQBzAHQAYQBiAGwAaQBzAGgAZQBkACIAfQAgAHwAIABTAGUAbABlAGMAdAAtAE8AYgBqAGUAYwB0ACAAIgBMAG8AYwBhAGwAQQBkAGQAcgBlAHMAcwAiACwAIAAiAEwAbwBjAGEAbABQAG8AcgB0ACIALAAgACIAUgBlAG0AbwB0AGUAQQBkAGQAcgBlAHMAcwAiACwAIAAiAFIAZQBtAG8AdABlAFAAbwByAHQAIgA=',
    b'WwBTAHkAcwB0AGUAbQAuAEUAbgB2AGkAcgBvAG4AbQBlAG4AdABdADoAOgBPAFMAVgBlAHIAcwBpAG8AbgAuAFYAZQByAHMAaQBvAG4AUwB0AHIAaQBuAGcA',
    b'RwBlAHQALQBOAGUAdABJAFAAQQBkAGQAcgBlAHMAcwAgAC0AQQBkAGQAcgBlAHMAcwBGAGEAbQBpAGwAeQAgAEkAUAB2ADQAIAB8ACAAUwBlAGwAZQBjAHQALQBPAGIAagBlAGMAdAAgAEkAUABBAGQAZAByAGUAcwBzAA==',
    b'RwBlAHQALQBDAGgAaQBsAGQASQB0AGUAbQAgAC0AUABhAHQAaAAgACIAQwA6AFwAUAByAG8AZwByAGEAbQAgAEYAaQBsAGUAcwAiACAAfAAgAFMAZQBsAGUAYwB0AC0ATwBiAGoAZQBjAHQAIABOAGEAbQBlAA==',
    b'RwBlAHQALQBDAGgAaQBsAGQASQB0AGUAbQAgAC0AUABhAHQAaAAgACcAQwA6AFwAUAByAG8AZwByAGEAbQAgAEYAaQBsAGUAcwAgACgAeAA4ADYAKQAnACAAfAAgAFMAZQBsAGUAYwB0AC0ATwBiAGoAZQBjAHQAIABOAGEAbQBlAA==',
    b'RwBlAHQALQBDAGgAaQBsAGQASQB0AGUAbQAgAC0AUABhAHQAaAAgACcAQwA6ACcAIAB8ACAAUwBlAGwAZQBjAHQALQBPAGIAagBlAGMAdAAgAE4AYQBtAGUA',
    b'RwBlAHQALQBOAGUAdABOAGUAaQBnAGgAYgBvAHIAIAAtAEEAZABkAHIAZQBzAHMARgBhAG0AaQBsAHkAIABJAFAAdgA0ACAAfAAgAFMAZQBsAGUAYwB0AC0ATwBiAGoAZQBjAHQAIAAiAEkAUABBAEQARAByAGUAcwBzACIA',
    b'RwBlAHQALQBOAGUAdABJAFAAQwBvAG4AZgBpAGcAdQByAGEAdABpAG8AbgAgAHwAIABGAG8AcgBlAGEAYwBoACAASQBQAHYANABEAGUAZgBhAHUAbAB0AEcAYQB0AGUAdwBhAHkAIAB8ACAAUwBlAGwAZQBjAHQALQBPAGIAagBlAGMAdAAgAE4AZQB4AHQASABvAHAA',
    b'RwBlAHQALQBEAG4AcwBDAGwAaQBlAG4AdABTAGUAcgB2AGUAcgBBAGQAZAByAGUAcwBzACAALQBBAGQAZAByAGUAcwBzAEYAYQBtAGkAbAB5ACAASQBQAHYANAAgAHwAIABTAGUAbABlAGMAdAAtAE8AYgBqAGUAYwB0ACAAUwBFAFIAVgBFAFIAQQBkAGQAcgBlAHMAcwBlAHMA'
    
]
for x in d:
    print(base64.b64decode(x).replace(b'\x00',b''))