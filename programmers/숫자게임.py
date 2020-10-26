def solution(A, B):
    answer = 0
    A.sort()
    B.sort()
    if min(A) > max(B) :
        return 0
    for i in A:
        for k in B:
            if i < k :
                answer += 1
                B.remove(k)
                break
    return answer