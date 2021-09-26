class Solution:
    def findMaxConsecutiveOnes(self, nums: list[int]) -> int:
        answer = 0
        continueTime = 0
        nums.append(0)
        for k in nums:
            if k == 1:
                continueTime += 1
            else:
                answer = max(answer, continueTime)
                continueTime = 0
        return answer
