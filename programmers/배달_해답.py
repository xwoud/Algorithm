import math
from collections import deque


def bfs(start, maps, distance, K):
    queue = deque()
    queue.append(start)

    distance[start] = 0

    while queue:
        y = queue.popleft()
        for x in range(1, len(maps)):
            if maps[y][x] != 0:
                if distance[x] > distance[y] + maps[y][x] and distance[y] + maps[y][x] <= K:
                    distance[x] = distance[y] + maps[y][x]
                    queue.append(x)

    return len([i for i in distance if i <= K])


def solution(N, road, K):
    distance = [math.inf for _ in range(N + 1)]

    # 마을 그래프 그리기
    maps = [[0 for _ in range(N + 1)] for _ in range(N + 1)]
    for frm, to, w in road:
        if maps[frm][to] == 0 and maps[to][frm] == 0:
            maps[frm][to], maps[to][frm] = w, w
        else:
            if w < maps[frm][to]:
                maps[frm][to], maps[to][frm] = w, w

    return bfs(1, maps, distance, K)