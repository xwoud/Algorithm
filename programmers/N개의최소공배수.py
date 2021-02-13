def gcd(a, b):
    if a % b == 0: return b
    else: return gcd(b, (a % b))

def solution(arr):
    while len(arr) > 1 :
        a, b = arr.pop(0), arr.pop(0)
        arr.append(a*b // gcd(a,b))
        arr.sort()

    return arr[0]

print(solution([2,6,8,14]))