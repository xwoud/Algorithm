def solution(answers):
    answer = []
    student1 = [1, 2, 3, 4, 5]
    student2 = [2, 1, 2, 3, 2, 4, 2, 5]
    student3 = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]
    num = [0,0,0]

    for i in range(0,len(answers),1):
        if answers[i] == student1[i%5] :
            num[0]+=1
        if answers[i] == student2[i%8] :
            num[1]+=1
        if answers[i] == student3[i%10] :
            num[2]+=1

    maxs = max(num)
    for i in range(0,len(num),1) :
        if num[i] == maxs :
            answer.append(i+1)

    return answer
