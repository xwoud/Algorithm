import sys

def get_divisor(n):
    divisors = []

    for i in range(1, int(n ** (1 / 2)) + 1):
        if (n % i == 0):
            divisors.append(i)
            if ((i ** 2) != n):
                divisors.append(n // i)

    divisors.sort()
    return divisors

N, K = map(int, sys.stdin.readline().split())
myDivisors = get_divisor(N)

if len(myDivisors) < K :
    print(0)
else:
    print(myDivisors[K-1])