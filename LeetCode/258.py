class Solution:
    def addDigits(self, num: int) -> int:

        if num < 10 : return num

        str_num = str(num)

        sum = 0
        for i in str_num:
            sum += int(i)

        return self.addDigits(sum)