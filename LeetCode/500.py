class Solution:
    def findWords(self, words: list[str]) -> list[str]:
        row = [[] for i in range(3)]
        row[0] = [i for i in "qwertyuiopQWERTYUIOP"]
        row[1] = [i for i in "asdfghjklASDFGHJKL"]
        row[2] = [i for i in "zxcvbnmZXCVBNM"]

        answer = []

        for word in words:

            if word[0] in row[0]: rowNum = 0
            elif word[0] in row[1]: rowNum = 1
            else: rowNum = 2

            for letter in word:
                if letter not in row[rowNum]:
                    break
            else:
                answer.append(word)

        return answer
