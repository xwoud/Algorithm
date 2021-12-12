from typing import List


class Solution:
    def isRectangleOverlap(self, rec1: List[int], rec2: List[int]) -> bool:
        x = min(rec1[2], rec2[2]) - max(rec1[0], rec2[0])
        
        # lowest top corner - highest bottom corner
        y = min(rec1[3], rec2[3]) - max(rec1[1], rec2[1])
        print(x,y)
        return x > 0 and y > 0


my = Solution()
print(my.isRectangleOverlap([0,0,2,2],[1,1,3,3]))