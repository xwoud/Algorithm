from typing import List


class Solution:
    def numberOfLines(self, widths: List[int], s: str) -> List[int]:
        lines = 1
        lastPixels = 0
    
        for char in s:
            pixel = widths[ord(char)-ord('a')]
            if lastPixels + pixel > 100: 
                lines += 1
                lastPixels = 0
            lastPixels += pixel
        return [lines, lastPixels]

my = Solution()
print(my.numberOfLines(widths=[10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10], s="abcdefghijklmnopqrstuvwxyz"))