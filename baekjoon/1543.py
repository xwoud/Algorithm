import sys

A = str(input(""))
B = str(input(""))
answer = 0

while A:
    if A[0:len(B)] == B :
        A = A[len(B):]
        answer += 1
    else :
        A = A[1:]
print(answer)