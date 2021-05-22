import sys

result = []

while True:
    stack = []
    count = 0
    s = sys.stdin.readline()
    if '-' in s:
        break

    for i in range(len(s)):
        if not stack and s[i] == '}':
            count += 1
            stack.append('{')
        elif stack and s[i] == '}':
            stack.pop()
        else:
            stack.append(s[i])
    count += len(stack)//2
    result.append(count)

for i in range(len(result)):
    print(i+1, '. ', result[i], sep='')