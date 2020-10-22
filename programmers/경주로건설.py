# -*- coding: utf-8 -*-
from collections import deque
dx = [1, 0, 0, -1] #사실상 y좌표
#동 남 북 서 = 오른쪽 아래 위 왼쪽
dy = [0, 1, -1, 0] #사실상 x좌표


def racing(n, x, y, board, cost, direction):
    cost[y][x] = 0
    # 들렸다는걸 표시해주는걸까??
    q = deque()
    # (현재 위치에서의 비용, x좌표, y좌표, 방향=내 시선)
    q.append((0, x, y, 0)) #동쪽(오른쪽)
    q.append((0, x, y, 1)) #남쪽(아래쪽)
    print(q)
    while q:
        curr_cost, x, y, d = q.popleft()
        for i in range(4): #동서남북으로 가기위해
            nx = x + dx[i]
            ny = y + dy[i]
            next_cost = 0
            if nx < 0 or ny < 0 or nx >= n or ny >= n or board[ny][nx] == 1:
            # 배열 밖으로 나가거나 이미 간 곳이면?
                continue
                # 계속하세요
            if i == d:
                # 직진이라면
                new_cost = 100
            else:
                # 고개를 돌려야한다면
                new_cost = 600
            #이제 그 다음까지 갔을 때 금액
            next_cost = new_cost + curr_cost
            if cost[ny][nx] == -1 or cost[ny][nx] >= next_cost:
                #다음 가는 곳이 안들렸던 곳이거나 다른 길로 갔던길이긴 하지만 지금이 더 쌀 경우
                cost[ny][nx] = next_cost
                #금액을 대체해줌. += 아님 =으로 해야한다.
                q.append((next_cost, nx, ny, i))


def solution(board):
    n = len(board)
    cost = [[-1] * n for _ in range(n)]
    racing(n, 0, 0, board, cost, 0)
    return cost[n - 1][n - 1]

print(solution([[0,0,0],[0,0,0],[0,0,0]]))