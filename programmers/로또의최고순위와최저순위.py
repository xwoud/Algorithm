def solution(lottos, win_nums):
    rank = [6, 6, 5, 4, 3, 2, 1]
    answer = []
    defalut = 0
    lottos.sort()

    for i in range(len(lottos)-1,-1,-1):
        if lottos[i] in win_nums:
            defalut += 1
            win_nums.remove(lottos[i])
            lottos.pop()
        elif lottos[i] != 0:
            lottos.pop()
    answer.append(rank[defalut])

    if len(lottos) <= len(win_nums):
        defalut += len(lottos)
    else :
        defalut += len(win_nums)

    answer.append(rank[defalut])

    answer.reverse()

    return answer