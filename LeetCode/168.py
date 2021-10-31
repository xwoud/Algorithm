class Solution:
    def convertToTitle(self, columnNumber: int) -> str:
        result = ""
        while (columnNumber > 0):
            endNumber = (columnNumber - 1) % 26
            columnNumber = (columnNumber - 1) // 26
            result = chr(endNumber + 65) + result
        return result