import sys

N = int(sys.stdin.readline())
arr = list(map(int, input().split()))

def getPrime(n):
    primes = [True] * n
    m = int(n ** 0.5)
    for i in range(2, m+1):
        if primes[i] == True:
            for j in range(i+i, n, i):
                primes[j] = False
    return [i for i in range(2,n) if primes[i] == True]

primeList = getPrime(max(arr)+1)
print(primeList)
# answer = 0
# for k in arr :
#     if k in primeList:
#         answer += 1
# print(answer)

# for k in arr:
#     a = [i for i in range(3,k+1,2)]
#     print(a)
# def getPrimeNum(n):
#     if n == 1 :
#         return False
#     elif n == 2 :
#         return True
#     for i in range(2, n):
#         if n % i == 0 :
#             return False
#     return True
#
# answer = 0
# for k in arr :
#     if getPrimeNum(k) :
#         answer += 1
#
# print(answer)