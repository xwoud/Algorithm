def solution(N, road, K):
    answer = 0
    MAX = 10000000
    graph = [[MAX for _ in range(N+1)] for _ in range(N+1)]

    for i in range(1, N+1):
        graph[i][i] = 0

    for connection in road:
        n1 = connection[0]
        n2 = connection[1]
        w = connection[2]
        if graph[n1][n2] > w:
            graph[n1][n2] = w
            graph[n2][n1] = w

    for x in range(1, N+1):
        for y in range(1, N+1):
            for i in range(1, N+1):
                graph[x][i] = min(graph[x][i], graph[x][y] + graph[y][i])

    answer = sum([1 if e <= K else 0 for e in graph[1]])

    return answer

#이것도 약간의 힌트를 보면서 푼거지만.. 저는 실패했습니다...