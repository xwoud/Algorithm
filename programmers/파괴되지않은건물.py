import numpy

def solution(board, skill):
    answer = 0
    n = len(board[0]) + 1
    m = len(board) + 1
    array = [[0 for col in range(n)] for row in range(m)]

    for point in skill:
        if point[0] == 1: degree = - point[5]
        else : degree = point[5]
        x1, y1 = point[1], point[2]
        x2, y2 = point[3], point[4]
        array[x1][y1] += degree
        array[x1][y2+1] -= degree
        array[x2+1][y1] -= degree
        array[x2+1][y2+1] += degree

    point = 0
    while point < n-1 :
        before = 0
        for i in range(n):
            array[point][i] += before
            before = array[point][i]
        point += 1
    
    point = 0
    while point < m-1 :
        before = 0
        for i in range(m):
            array[i][point] += before
            before = array[i][point]
        point += 1
    
    for i in range(m-1):
        for j in range(n-1):
            if board[i][j] + array[i][j] > 0 : answer += 1
    return answer