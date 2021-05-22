n, s = map(int, input().split())
num = list(map(int, input().split()))

start = 0
end = 0
answer = num[0]
cnt = 1
mini = 1000001

while start < n:

    if answer >= s:
        mini = min(mini, cnt)

    if answer >= s or end == n - 1:
        answer -= num[start]
        start += 1
        cnt -= 1

    else:
        end += 1
        answer += num[end]
        cnt += 1

if mini == 1000001 :
    mini = 0

print(mini)