def solution(tickets):
    routes = {}
    for t in tickets:
        routes[t[0]] = routes.get(t[0], []) + [t[1]]

    for r in routes:
        routes[r].sort(reverse=True)

    start = ["ICN"]
    path = []
    
    while len(start) > 0:
        top = start[-1]
        if top not in routes or len(routes[top]) == 0:
            path.append(start.pop())
        else:
            start.append(routes[top][-1])
            routes[top] = routes[top][:-1]

    answer = path[::-1]
    return answer