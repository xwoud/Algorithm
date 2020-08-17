def solution(numbers, target):
    answer = 0
    all_plus= [0]
    for i in numbers:
        sub = []
        for j in all_plus :
            sub.append(j+i)
            sub.append(j-i)
        all_plus = sub
    answer = all_plus.count(target)
    return answer