def solution(n):
    answer = 0
    for i in range(1,n//2+1):
        sums = 0
        for j in range(i,n+1):
            sums += j
            if sums == n :
                answer += 1
                break
            elif sums > n :
                break
    answer += 1
    return answer
print(solution(15))