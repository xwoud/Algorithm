class Solution:
    def searchInsert(self, nums: list[int], target: int) -> int:

        for i in range(0, len(nums),1):
            if nums[i] == target:
                return i
            elif nums[i] > target:
                return i
        return len(nums)

