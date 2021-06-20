class Solution:
    def generate(self, numRows: int) -> List[List[int]]:

        if numRows == 1:
            return [[1]]

        answer = []

        for i in range(1, numRows + 1):
            answer.append([0] * i)
        for i in range(0, numRows):
            answer[i][0] = 1
            answer[i][-1] = 1

        for i in range(1, numRows):
            for j in range(0, len(answer[i]), 1):
                if answer[i][j] == 0:
                    answer[i][j] = answer[i - 1][j - 1] + answer[i - 1][j]

        return answer
