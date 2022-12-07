import re
code = open("code.js",'r').readlines()
def find(s,l):
    s = str(s)
    for i in l:
        if ("case "+s+":") in i:
            return l.index(i)
def clean_code(code):
    if "^" not in code:
        blacklist = "();\n"
        for c in blacklist:
            code = code.replace(c,'')
        code = code + '\n' + code[0:5] + " &= 0xff"
    code = code.replace(";\n",'').replace("))",")")
    return code+"\n"

ls_stage = [int(i.rstrip("\n")) for i in open("stageNums.txt" ,'r').readlines()]
ls_random = [float(i.rstrip("\n")) for i in open("randomNumbers.txt" ,'r').readlines()]
ifelse = [int(i[0]) for i in open("ifelse.txt",'r').readlines()]
print(ifelse)
rd_idx =0
st_idx = 0
sm_idx = 0
res = []
c = 0

while True:
    # math.random()*2**30 use 1 random
    rd_idx+=1

    if ls_stage[st_idx]==185078700:
        break
    case_idx = find(ls_stage[st_idx],code)      # return index of " case xxxxxxx: " im codes
    st_idx+=1
    statement = ""
    if "0.5" in code[case_idx+1]:
        rd_idx +=1
    if ifelse[sm_idx]:
        statement = code[case_idx+2]
    else:
        if "else" in code[case_idx+4]:
            statement = code[case_idx+5]
        else:
            statement = code[case_idx+4]
    sm_idx+=1

    statement = statement.strip(" ")
    if 'Math.floor(Math.random() * 256)' in statement:
        statement = statement.replace('Math.floor(Math.random() * 256',str(int(ls_random[rd_idx]*256)))
        rd_idx+=1
    statement = clean_code(statement)
    # reverse
    # if "+=" in statement:
    #     statement = statement.replace("+=","-=")
    # elif "-=" in statement:
    #     statement = statement.replace("-=","+=")
    res.append(statement)

f = open('result.txt','w')
f.write(''.join(res[::-1]))
