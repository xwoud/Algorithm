from itertools import combinations

def solution(n, data, limit):
    # data = [이름, 해결문제번호, 필요시간, 필요공간]
    # limit = 총 시간, 저장공간정보 (0은 한계가 없다는 뜻)

    answer = []
    additData = []
    for i in data:
        additData.append(i.split())

    limit = limit.split()

    k = 0

    combinationsList = [] # 조합을 저장하는 배열

    while (k != len(data)) :
        asset = additData[k]
        # 기준 값을 먼저 잡음
        ex = additData[:]
        ex.pop(k)
        testList = []

        for i in range(len(ex)-1,-1,-1):
            if ex[i][1] != asset[1] :
                # 기준 값과 문제 번호가 다르다면 후보 리스트로 넣어줌
                testList.append(ex[i][0])

        if n == 2 :

            for i in range(0,len(testList),1):
                my = [asset[0],testList[i]]
                my.sort()
                if my not in combinationsList:
                    # 중복 후보를 피하기 위한 if 문
                    combinationsList.append([asset[0],testList[i]])
        else :

            a = list(combinations(testList,n-1))
            # 조합을 구해줌
            good = [asset[0]]
            for i in range(len(a[0])):
                good.append(a[0][i])
            good.sort()
            if good not in combinationsList:
                combinationsList.append(good)

        k += 1

    for mData in combinationsList:
        # 후보 리스트들의 시간과 공간을 검사하는 for문
        time = 0
        space = 0
        for j in mData:
            for k in additData:
                if k[0] == j :
                    time += int(k[2])
                    space += int(k[3])
                    break
        mData.append(time)
        mData.append(space)

    for mData in combinationsList:
        if (mData[-2] <= int(limit[0]) or int(limit[0]) == 0) and (mData[-1] <= int(limit[1]) or int(limit[1]) == 0):
            # 시간과 공간이 넘치지 않는 것을 최종 정답 후보로 올림
            answer.append(mData)

    if len(answer) == 0 :
        return []
    elif len(answer) == 1 :
        return answer[0][:n]
    else :
        limitTotal = answer[0][-1] + answer[0][-2]
        totalAnswer = answer[0]

        for i in answer:
            if i[-1]+i[-2] < limitTotal:
                limitTotal = i[-1]+i[-2]
                totalAnswer = i
        return totalAnswer[:n]