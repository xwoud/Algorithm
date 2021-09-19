class Solution:
    def firstUniqChar(self, s: str) -> int:
        new_list = {}
        for i in s:
            try:
                new_list[i] += 1
            except:
                new_list[i] = 1

        for key, value in new_list.items():
            if value == 1: return s.find(key)

        return -1