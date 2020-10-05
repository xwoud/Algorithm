def solution(n, results):
    answer = 0
    wins, loses = {},{}
    for i in range(0,n+1):
        wins[i], loses[i] = set(), set()

    for i in range(1,n+1):
        for j in results:
            if j[0] == i:
                wins[i].add(j[1])
            if j[1] == i:
                loses[i].add(j[0])
        for k in loses[i]:
            wins[k].update(wins[i])
        for k in wins[i]:
            loses[k].update(loses[i])
            
    for i in range(1,n+1):
        if len(wins[i]) + len(loses[i]) == n - 1:
            answer += 1

    return answer
