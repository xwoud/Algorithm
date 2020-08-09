def solution(progresses, speeds):
    answer = []
    N = len(progresses)
    pass_answer = 0
    while N!=pass_answer :
        tmp = 0

        for i in range(pass_answer,N,1):
            progresses[i] += speeds[i]

        if progresses[pass_answer] >= 100 :
            for i in range(pass_answer,N):
                if progresses[i] >= 100:
                    tmp += 1
                else :
                    break
            answer.append(tmp)

            pass_answer+=tmp

            
    return answer