class Solution:
    def findTheDifference(self, s: str, t: str) -> str:

        s = sorted(list(s))
        t = sorted(list(t))
        lengthString = len(t)
        i = 0

        while (i < lengthString - 1) and (s[i] == t[i]):
            i += 1
        return t[i]