import sys

from collections import deque

def find_answer(a):
    visited = []

    myQ = deque()
    myQ.append([0,a])
    visited.append(a)

    while myQ:
        count, num = myQ.popleft()

        if num == b:
            return count + 1

        for next in (num * 2, int(str(num) + "1")):
            if next <= b:
                if next not in visited:
                    myQ.append([count + 1, next])
                    visited.append(next)

    return -1

a,b = map(int, sys.stdin.readline().split())
answer = find_answer(a)

print(answer)
