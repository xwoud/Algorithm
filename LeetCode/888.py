from typing import List

class Solution:
    def fairCandySwap(self, aliceSizes: List[int], bobSizes: List[int]) -> List[int]:
        ta, tb, bobSizes = sum(aliceSizes), sum(bobSizes), set(bobSizes)
        after = (ta + tb) // 2

        for e in aliceSizes:
            if (expected := after - (ta - e)) in bobSizes:
                return [e, expected]