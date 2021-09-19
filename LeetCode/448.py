class Solution:
    def findDisappearedNumbers(self, nums: list[int]) -> list[int]:
        output = []
        s = set(nums)
        for i in range(1, len(nums) + 1):
            if not i in s:
                output.append(i)
        return output
