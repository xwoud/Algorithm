from typing import List


class Solution:
    def largeGroupPositions(self, s: str) -> List[List[int]]:
        res = []
        s += '0'
        start = 0
        for i in range(1,len(s)):
            if s[i] != s[i-1]:
                res.append([start,i-1])
                start = i
        return list(filter(lambda x: abs(x[0]-x[1]) > 2, res))
        