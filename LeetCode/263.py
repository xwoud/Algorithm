class Solution:
    def isUgly(self, n: int) -> bool:
        if not n:
            return None

        factors = [2,3,5]

        for factor in factors:
            while n%factor == 0:
                n //= factor
            if n == 1:
                return True
        return False