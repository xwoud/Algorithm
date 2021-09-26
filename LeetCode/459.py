class Solution:
    def repeatedSubstringPattern(self, s: str) -> bool:
        answer = []
        for i in range(0, len(s)):
            if s[0:i + 1] * (len(s) // (i + 1)) == s:
                answer.append([s[0:i + 1], (len(s) // (i + 1))])
        return (len(answer) > 1)
