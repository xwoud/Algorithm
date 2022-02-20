from typing import List

class Solution:
    def smallestRangeI(self, nums: List[int], k: int) -> int:

        minScore = min(nums) + k
        maxScore = max(nums) - k
        if minScore > maxScore:
            return 0
        else:
            return maxScore - minScore