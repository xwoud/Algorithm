def solution(n, queries):
    answer = []
    global test

    test = []
    for _ in range(n):
        test.append([])
    push(1,4)
    push(2,2)
    push(1,3)
    push(1,6)
    pop(3)
    pop(2)
    print(test)
    return answer


def solution(n, queries):
    answer = []
    return answer


def myPush(arrayNum, num):
    total = 0
    for i in range(0, len(test), 1):
        total += len(test[i])

    if total == 0:
        for i in test:
            i.append(num)
    else:
        test[arrayNum - 1].append(num)


def myPop(num):
    if len(test[num - 1]) == 1:
        for i in range(0, len(test), 1):
            test[i].pop(0)

        newAsset = test[num - 1 - 2][0]
        for i in range(0, len(test), 1):
            test[i].insert(0, newAsset)
        test[num - 1 - 2].pop(0)

    else:
        test[num - 2].pop()