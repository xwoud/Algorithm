def solution(arr1, arr2):
    answer = [[0 for col in range(len(arr2[0]))] for row in range(len(arr1))]

    for i in range(len(answer)):
        for j in range(len(answer[0])):
            for t in range(len(arr2)):
                answer[i][j] += arr1[i][t] * arr2[t][j]

    return answer