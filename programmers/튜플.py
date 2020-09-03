def solution(s):
    answer = []
    tuple = s[2:-2]
    tuple = tuple.split("},{")
    tuple.sort(key=len)
    for i in tuple:
        k = i.split(',')
        for j in k:
            if int(j) not in answer:
                answer.append(int(j))
    return answer
