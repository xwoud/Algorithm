class Solution:
    def isHappy(self, n: int) -> bool:
        squareSum = 0

        for j in range(8):
            squareSum = (sum(int(i) ** 2 for i in list(str(n))))

            if (squareSum == 1):
                return True
            else:
                n = squareSum

        return False