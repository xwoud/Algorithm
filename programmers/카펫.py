def solution(brown, yellow):
    answer = []
    list = []
    for i in range(yellow,0,-1):
        if yellow//i > i :
            break
        if yellow % i == 0 :
            list.append([i,yellow//i])

    while list :
        min = list.pop()
        if (min[0]+2) * (min[1]+2) == brown+yellow :
            answer = [min[0]+2,min[1]+2]
            break

    return answer
