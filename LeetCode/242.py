class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        dict1 = {}
        dict2 = {}

        for i in set(list(t)):
            dict2[i] = t.count(i)

        for i in set(list(s)):
            dict1[i] = s.count(i)

        dict1 = sorted(dict1.items())
        dict2 = sorted(dict2.items())

        if dict1 == dict2: return True
        else : return False
