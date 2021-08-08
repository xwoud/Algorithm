from collections import Counter

class Solution:
    def majorityElement(self, nums: list[int]) -> int:

        return (Counter(nums).most_common()[0][0])
