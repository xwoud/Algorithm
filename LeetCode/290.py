class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        word = s.split()

        if len(pattern) != len(word): return False
        dic = {}

        for i in range(0,len(pattern),1):
            if (pattern[i] not in dic.keys()):
                if word[i] in dic.values(): return False
                else : dic[pattern[i]] = word[i]
            elif not dic[pattern[i]] == word[i]:
                return False
        return True