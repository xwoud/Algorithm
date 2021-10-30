class Solution:
    def calPoints(self, ops: list[str]) -> int:
        score = []
        for i in range(len(ops)):
            if ops[i] == 'C':
                score.pop()
            elif ops[i] == 'D':
                score.append(2 * score[-1])
            elif ops[i] == '+':
                score.append(score[-1] + score[-2])
            else:
                score.append(int(ops[i]))
        return sum(score)