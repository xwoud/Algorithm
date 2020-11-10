import sys
from collections import deque

case = int(sys.stdin.readline())
for i in range(case):
    n, m = map(int, sys.stdin.readline().split())
    arr = deque(map(int, sys.stdin.readline().split()))
    check = [False]*n
    check[m] = True
    if n == 1 :
        print(1)
    else :
        count = 0
        while True in check:
            if arr[0] >= max(arr):
                arr.popleft()
                check.pop(0)
                count += 1
            else:
                arr.append(arr.popleft())
                check.append(check.pop(0))
        print(count)