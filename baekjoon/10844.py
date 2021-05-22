import sys

N = int(sys.stdin.readline())

candi_list = [[0 for i in range(10)] for j in range(N+1)]

for i in range(1, 10):
    candi_list[1][i] = 1

for i in range(2, N + 1):
    for j in range(10):
        if j == 0:
            candi_list[i][j] = candi_list[i - 1][1]
        elif j == 9:
            candi_list[i][j] = candi_list[i - 1][8]
        else:
            candi_list[i][j] = candi_list[i - 1][j - 1] + candi_list[i - 1][j + 1]

print(sum(candi_list[N]) % 1000000000)

