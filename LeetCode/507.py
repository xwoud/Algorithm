class Solution:
    def getMyDivisor(self, n: int):

        divisorsList = []

        for i in range(1, int(n ** (1 / 2)) + 1):
            if (n % i == 0):
                divisorsList.append(i)
                if ((i ** 2) != n):
                    divisorsList.append(n // i)

        divisorsList.sort()
        return divisorsList

    def checkPerfectNumber(self, num: int) -> bool:

        divisors = self.getMyDivisor(num)
        divisors.pop()
        if sum(divisors) == num: return True
        else: return False
my = Solution()
print(my.getMyDivisor(n=18))
