class Solution:
    def myPow(self, x: float, n: int) -> float:
        
        if n == 0:
            return 1

        if n < 0:
            x = 1 / x
            n = -n

        y = 1

        while n > 1:
            if n % 2 == 0:
                x = x * x
                n = n / 2
            else:
                y = x * y
                x = x * x
                n = (n - 1) / 2

        return x * y
