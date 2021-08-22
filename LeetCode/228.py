class Solution:
    def summaryRanges(self, nums: list[int]) -> list[str]:
        answer = []
        start = 0
        end = 0

        while start < len(nums):
            while end + 1 < len(nums) and nums[end + 1] == nums[end] + 1:
                end += 1
            answer.append(f"{nums[start]}->{nums[end]}" if start != end else f"{nums[start]}")
            start = end + 1
            end = start

        return answer
