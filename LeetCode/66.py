class Solution:
    def plusOne(self, digits: list[int]) -> list[int]:

        for i in range(len(digits)-1,-1,-1):
            digits[i] = digits[i] + 1
            if digits[i] < 10 :
                break
            else :
                digits[i] = 0
                if i == 0 :
                    digits.insert(0,1)


        return digits

my = Solution()
print(my.plusOne([8,9,9,9]))