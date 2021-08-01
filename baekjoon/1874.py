import sys

n = int(sys.stdin.readline())
r_answer = [int(sys.stdin.readline().rstrip()) for _ in range(n)]
arr = []
push = []

for i in range(1,n+1,1):
    if len(arr) == 0 :
        arr.append(i)
        push.append("+")
    else :
        while len(arr)>0 and arr[-1] == r_answer[0] :
            arr.pop()
            r_answer.pop(0)
            push.append("-")
        arr.append(i)
        push.append("+")

if len(r_answer) > 0 and arr[::-1] == r_answer :
    for i in range(len(r_answer)):
        push.append("-")
    r_answer = []

if len(r_answer) != 0 :
    print("NO")
else :
    for i in push:
        print(i)
