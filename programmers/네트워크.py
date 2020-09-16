def solution(n, computers):
    answer = 0
    bfs = []
    lists = [0]*n

    while 0 in lists:
        bfs.append(lists.index(0))
        while bfs:
            node = bfs.pop(0)
            lists[node] = 1
            for i in range(n):
                if lists[i] == 0 and computers[node][i] == 1:
                    bfs.append(i)
        answer += 1
    return answer