import sys

answer = []

N = int(sys.stdin.readline())
numbers = list(map(int, input().split()))
add, sub, mul, div = map(int, input().split())

answer_min = 1e9
answer_max = -1e9

def dfs(i, res, add, sub, mul, div):

    global answer_min, answer_max

    if (add+sub+mul+div) == 0:
        answer_max = max(res, answer_max)
        answer_min = min(res, answer_min)
        return

    else:
        if add:
            dfs(i+1, res+numbers[i], add-1, sub, mul, div)
        if sub:
            dfs(i+1, res-numbers[i], add, sub-1, mul, div)
        if mul:
            dfs(i+1, res*numbers[i], add, sub, mul-1, div)
        if div:
            dfs(i+1, int(res/numbers[i]), add, sub, mul, div-1)

dfs(1, numbers[0], add, sub, mul, div)

print(answer_max)
print(answer_min)