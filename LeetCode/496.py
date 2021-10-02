class Solution:
    def nextGreaterElement(self, nums1: list[int], nums2: list[int]) -> list[int]:
        nextNumber = {}
        for i in range(len(nums2)):
            for j in range(i + 1, len(nums2)):
                if nums2[j] > nums2[i]:
                    nextNumber[nums2[i]] = nums2[j]
                    break
        for i in range(len(nums1)):
            nums1[i] = nextNumber.get(nums1[i], -1)
        return nums1

