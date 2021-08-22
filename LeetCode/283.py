class Solution:
    def moveZeroes(self, nums: list[int]) -> None:
        nums[:] = [i for i in nums if i != 0] + [0] * nums.count(0)
        return nums