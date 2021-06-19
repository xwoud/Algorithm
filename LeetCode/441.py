class Solution:
    def arrangeCoins(self, n: int) -> int:
        if n == 1: return n

        left = 0
        right = n

        ans = 0

        while (left <= right):
            mid = (left + right) // 2
            sum = mid * (mid + 1) // 2
            if (sum <= n):
                ans = mid
                left = mid + 1
            else:
                right = mid - 1

        return ans
