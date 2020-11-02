import sys
a = str(sys.stdin.readline().rstrip())

result = ""
start = 0
end = 0
flag = False
strings = ''

for i in range(0,len(a),1):
    if flag == False :
        if a[i] == "<":
            result += strings[::-1]
            strings = ""
            start = i
            flag = True
        elif a[i] == " ":
            result += strings[::-1] + " "
            strings = ""
        else :
            strings += a[i]
    else:
        if a[i] == ">":
            end = i
            result += a[start:end+1]
            flag = False

if len(strings) != 0 :
    result += strings[::-1]

print(result)

