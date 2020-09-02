def solution(s):
    n = len(s) // 2
    minv = float('inf')
    if len(s) == 1: return 1

    for i in range(1, n + 1):
        alist = []
        blist = []
        for j in range(0, len(s), i):
            if alist:
                if s[j:j + i] == alist[-1]:
                    blist[-1] += 1
                else:
                    alist.append(s[j:j + i])
                    blist.append(1)
            else:
                alist.append(s[j:j + i])
                blist.append(1)

        temp = sum(map(len, alist)) + sum(map(lambda y: len(str(y)), filter(lambda x: x > 1, blist)))
        minv = min(minv, temp)
    return minv
