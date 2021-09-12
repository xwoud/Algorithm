class Solution:
    def intersection(self, nums1: list[int], nums2: list[int]) -> list[int]:
        if len(nums1) > len(nums2) :
            nums1, nums2 = nums2, nums1

        answer = list(filter(lambda x: x in nums2, nums1))
        return list(dict.fromkeys(answer))