def solution(a):
    answers = 2
    if 0 <= len(a) <= 2:
        return len(a)
    left = a[0]
    right = a[-1]

    for i in range(1, len(a) - 1):
        if left > a[i]:
            left = a[i]
            answers += 1
        if right > a[-1 - i]:
            right = a[-1 - i]
            answers += 1

    if left == right:
        return answers - 1

    else:
        return answers

print(solution([-16,27,65,-2,58,-92,-71,-68,-61,-33]))