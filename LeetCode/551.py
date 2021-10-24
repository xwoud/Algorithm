class Solution:
    def checkRecord(self, s: str) -> bool:
        count = 0
        for i in range(len(s)):
            if s[i] == 'A':
                count += 1
            if count == 2:
                return False
            if s[i] == 'L' and i <= len(s) - 3:
                if s[i + 1] == 'L' and s[i + 2] == 'L':
                    return False
        return True