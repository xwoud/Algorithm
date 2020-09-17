import fractions
def solution(N, stages):
    answer = []
    for i in range(1,N+1,1):
        denominator = 0
        numerator = 0
        for j in stages:
            if j == i :
                numerator += 1
            if j >= i :
                denominator += 1
        if denominator == 0 :
            answer.append([-1, i])
        else :
            answer.append([fractions.Fraction(numerator,denominator),i])

    k = sorted(answer, key = lambda x : (-x[0], x[1]))
    answer = []
    for i in k :
        answer.append(i[1])

    return answer