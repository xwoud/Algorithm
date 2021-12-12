from typing import List


class Solution:
    def shortestToChar(self, s: str, c: str) -> List[int]:
        locations = list(filter(lambda x: s[x] == c, range(len(s))))
        n = len(locations) - 1
        currentC = 0
        result = []

        for i, char in enumerate(s):
            dist1 = abs(i - locations[currentC])
            if currentC != n:
                dist2 = abs(i - locations[currentC+1])
                if dist1 > dist2:
                    currentC += 1
                    dist1 = dist2
            result.append(dist1)
        return result