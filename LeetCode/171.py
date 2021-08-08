class Solution:
    def titleToNumber(self, columnTitle: str) -> int:
        sum = 0
        for i in range(len(columnTitle)):
            sum = (sum * 26) + ord(columnTitle[i]) - 64
            print(i, sum)
        return sum