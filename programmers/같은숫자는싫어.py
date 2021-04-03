def solution(arr):
    before = -1
    answer = []
    for i in arr :
        if i != before :
            answer.append(i)
        before = i
    return answer

print(solution([4,4,4,3,3]))