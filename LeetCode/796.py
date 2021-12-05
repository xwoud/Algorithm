class Solution:
    def rotateString(self, s: str, goal: str) -> bool:
        if s == goal: return True
        
        n = 1
        while n<len(s):
            s = s[1:] + s[0]
            if s == goal: return True
            n += 1
        return False