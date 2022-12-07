f = open("code.js",'r').read()
f = f.split("continue;")
print(f[::-1])