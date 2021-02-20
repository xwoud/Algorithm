def solution(n, s):
    answer = []

    if s < n :
        return [-1]

    for _ in range(n):
        answer.append(s//n)

    indexs = len(answer)-1

    for i in range(s - sum(answer)):
        answer[indexs] += 1
        indexs -= 1

    return answer