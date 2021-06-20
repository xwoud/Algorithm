class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        if len(flowerbed) < n:
            return False

        flowerbed.insert(0, 0)
        flowerbed.append(0)

        length = len(flowerbed)
        flower = 0
        idx = 1

        while idx < length - 1:
            if flowerbed[idx - 1:idx + 2] == [0, 0, 0]:
                flower += 1
                idx += 2
            else:
                idx += 1

        return flower >= n