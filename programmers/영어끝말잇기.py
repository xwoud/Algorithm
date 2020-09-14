def solution(n, words):
    answer = [[0 for x in range(1)] for y in range(n)]

    for i in range(0,len(words),1):
        answer[i%n].append(words[i])
        if answer[i%n][0] == 0 :
            answer[i%n].pop(0)

    last = answer[0][0][:1]
    used = []

    for j in range(0,len(answer[0]),1):
        for k in range(0,n,1):
            if (answer[k][j][:1] == last) and (len(answer[k][j])>1) and (answer[k][j] not in used) :
                last = answer[k][j][len(answer[k][j]) - 1:]
                used.append(answer[k][j])
            else :
                return [k+1,j+1]


    return [0,0]
