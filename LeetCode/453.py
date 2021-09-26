import sys

class Solution:
    def minMoves(self, nums: list[int]) -> int:
        num_min = sys.maxsize
        sum = 0
        for i in nums:
            if i<num_min: num_min = i
            sum += i
        return sum - num_min*len(nums)
