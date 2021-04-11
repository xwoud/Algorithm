import sys

N = int(sys.stdin.readline())
answer = []

def check(N) :
    k = str(N)
    for i in range(0,len(k)-1):
        if k[i] <= k[i+1]:
            test = int(str(k[:i]) + str(int(k[i])+1)+ str(0) + str(k[i+2:]))
            return (False,test)
    return (True,N+1)

i = 0

while (len(answer) != (N+1)):
    if len(answer) == 1023 :
        break
    a,b = check(i)
    if a == True :
        answer.append(i)
    i = b

if len(answer) == (N+1) :
    print(answer[N])
else:
    print("-1")

