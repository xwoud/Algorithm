#틀린 민희 풀이..

def solution(name):
    answer = 0
    answerKey = [] #name으로 설정되어있
    num = [0] * len(name)
    for i in name:
        answerKey += [i]
    for j in range(0,len(answerKey),1) :
        if ord(answerKey[j])-ord('A') <= ord('Z') - ord(answerKey[j]) :
            num[j] = ord(answerKey[j]) - ord('A')
        else :
            num[j] = ord('Z') - ord(answerKey[j]) + 1
    if min(num) == 0 :
        answer = len(num) - num.count(0) - 1
    else :
        answer = (len(num)-1)
    while num :
        i = 0
        if num[i] == 0 :
            num.pop(i)
        else :
            answer += num[i]
            num.pop(i)
    return answer

