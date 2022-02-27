from math import fabs
from typing import List

class Solution:
    def isMonotonic(self, nums: List[int]) -> bool:
        increasing = True
        decreasing = True

        for i in range(0, len(nums)-1):
            if nums[i] < nums[i+1]: 
                increasing = False
            if nums[i] > nums[i+1]:
                decreasing = False

        return increasing or decreasing