class Solution:
    def missingNumber(self, nums: list[int]) -> int:

        nums.sort()

        for i in range(0, nums[-1] + 1, 1):
            if i != nums[i]:
                return i

        return nums[-1]+1