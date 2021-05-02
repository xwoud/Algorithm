import sys

n = int(sys.stdin.readline())

friends = dict()

for _ in range(n):
    a, b = map(str, sys.stdin.readline().split())
    if b == "enter":
        friends[a] = True
    else :
        del friends[a]

print("\n".join(sorted(friends.keys(), reverse=True)))
