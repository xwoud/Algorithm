import sys

def gcd(a,b):
    if a%b == 0 :
        return b
    elif b == 0 :
        return a
    else :
        return gcd(b,a%b)

def lcm(a,b):
    return a*b // gcd(a,b)

n,m = map(int, sys.stdin.readline().split())
print(gcd(n,m), lcm(n,m))