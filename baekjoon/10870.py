import sys

## 재귀 함수 사용
def getFibo(n):
    if n <= 1 :
        return n
    return getFibo(n - 1) + getFibo(n - 2)

N = int(sys.stdin.readline())
print(getFibo(N))

## for 문 사용
# fibo = [0,1]
# N = int(sys.stdin.readline())
# for i in range(2,N+1):
#     fibo.append(fibo[i-2]+fibo[i-1])
# print(fibo[N])