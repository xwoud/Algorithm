import sys

def getBinaryNum(n, lists):
    a, b = divmod(n, 2)
    lists.append(b)
    if a == 0 :
        return lists
    else :
        return getBinaryNum(a, lists)

T = int(sys.stdin.readline())

for _ in range(T) :
    n = int(sys.stdin.readline())
    answerList = []
    answer = getBinaryNum(n,answerList)
    for i in range(len(answer)):
        if answer[i] == 1:
            print(i, end = ' ')