
class Solution:
    def pivotIndex(self, nums: list[int]) -> int:
        right_sums = {}
        current_sum = 0

        for i in range(len(nums) - 1, -1, -1):
            right_sums[i] = current_sum
            current_sum += nums[i]
        current_sum = 0
        for i in range(len(nums)):
            if current_sum == right_sums[i]:
                return i
            current_sum += nums[i]

        return -1