import sys
from collections import deque

dx = [1, 0, 0, -1]
dy = [0, 1, -1, 0]
N, M = map(int, sys.stdin.readline().split())
count = [[0] * M for _ in range(N)]
arr = [list(map(int,sys.stdin.readline().rstrip())) for _ in range(N)]

def bfs():
    need_visit = deque()
    need_visit.append((0,0))
    while need_visit:
        now_pos = need_visit.popleft()
        if now_pos == (N-1,M-1):
            print(count)
            return count[now_pos[0]][now_pos[1]]
        for i in range(4):
            nx = now_pos[0] + dx[i]
            ny = now_pos[1] + dy[i]
            if nx >= 0 and ny >= 0 and nx < N and ny < M and arr[nx][ny] == 1:
                if not count[nx][ny] or count[nx][ny] > count[now_pos[0]][now_pos[1]] + 1 :
                    count[nx][ny] = count[now_pos[0]][now_pos[1]] + 1
                    need_visit.append((nx,ny))
print(bfs())