def solution(absolutes, signs):
    answer = 0
    for i in range(0,len(absolutes),1):
        if signs[i] == True:
            answer += absolutes[i]
        else :
            answer -= absolutes[i]
    return answer
