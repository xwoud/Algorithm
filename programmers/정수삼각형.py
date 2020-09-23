def solution(triangle):
    answer = 0
    for i in range(1,len(triangle),1):
        for j in range(i+1):
            if j == 0 :
                triangle[i][j] += triangle[i-1][j]
            elif j == i :
                triangle[i][j] += triangle[i-1][j-1]
            else :
                if triangle[i - 1][j-1] > triangle[i-1][j] :
                    triangle[i][j] += triangle[i-1][j - 1]
                else :
                    triangle[i][j] += triangle[i-1][j]

    answer = max(triangle[-1])
    return answer

solution([[7], [3, 8], [8, 1, 0], [2, 7, 4, 4], [4, 5, 2, 6, 5]])