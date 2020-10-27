def solution(words, queries):
    answer = [0]*len(queries)
    words.sort()
    t = 0
    for i in queries:
        for j in words:
            if len(j) == len(i):
                if (i[0] == "?") and (i[i.rindex("?")+1:] == j[i.rindex("?")+1:]) :
                    answer[t] += 1
                elif (i[0] != "?") and i[:i.index("?")] == j[:i.index("?")] :
                    answer[t] += 1
        t += 1
    return answer