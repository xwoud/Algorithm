def solution(s):
    answer = []
    if len(s) == 1:
        return 1
    for i in range(len(s) - 1):
        for j in range(i + 2, len(s) + 1):
            origin = s[i: j]
            if origin == origin[::-1]:
                answer.append(len(origin))
    if len(answer) == 0:
        return 1
    return max(answer)
