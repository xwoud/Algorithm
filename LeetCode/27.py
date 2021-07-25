class Solution:
    def removeElement(self, nums: list[int], val: int) -> int:

        if len(nums) == 0:
            return 0

        judge = len(nums)

        for i in range(judge):
            if nums[i] == val:
                nums[i] = float('inf')
                judge -= 1

        nums.sort()

        while nums[-1] == float('inf'):
            nums.pop()
            if len(nums) == 0 :
                break
        return judge
