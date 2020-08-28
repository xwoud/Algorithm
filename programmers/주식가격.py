def solution(prices):
    answer = []
    for i in range(0,len(prices),1):
        k = 0
        for j in range(i+1,len(prices),1):
            if prices[i] > prices[j] :
                k = 1
                answer.append(j-i)
                break
        if k == 0:
            answer.append(len(prices)-i-1)

    return answer

print(solution([1, 2, 3, 2, 3, 3, 1]))