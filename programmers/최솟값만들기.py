def solution(A,B):
    answer = 0
    A.sort(reverse=True)
    B.sort(reverse=False)
    for i in range(0,len(A),1):
        answer += A[i]*B[i]
    return answer