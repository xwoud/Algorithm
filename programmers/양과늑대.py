def solution(info, edges):
    global answer, graph
    answer = 0
    graph = [[] for _ in range(len(info))]
    for i in edges:
        graph[i[0]].append(i[1])
    dfs(0, 0, 0, [], info)
    return answer


def dfs(node, sheep, wolf, point, info) :
    global answer, graph
    if info[node] == 0 : 
        sheep += 1
    else: 
        wolf += 1
    if answer < sheep: 
        answer = sheep
    if wolf >= sheep: 
        return
    
    for i in graph[node]:
        point.append(i)
    for i in point:
        sub_point = point[:]
        sub_point.remove(i)
        dfs(i, sheep, wolf, sub_point, info)