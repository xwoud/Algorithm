class Solution:
    def addStrings(self, num1: str, num2: str) -> str:

        i = 0
        length_num1 = len(num1)
        length_num2 = len(num2)
        add = 0
        ans = ""

        while (i < length_num1 and i < length_num2): # num1, num2 둘 다 더할 것이 남았을 때
            x = ord(num1[length_num1 - 1 - i]) - ord("0")
            y = ord(num2[length_num2 - 1 - i]) - ord("0")
            t = x + y + add
            add = t // 10
            ans = str(t % 10) + ans
            i += 1

        while (i < length_num1): # num1만 더할 것이 남았을 때
            x = ord(num1[length_num1 - 1 - i]) - ord("0")
            t = x + add
            add = t // 10
            ans = str(t % 10) + ans
            i += 1

        while (i < length_num2): # num2만 더할 것이 남았을 때
            x = ord(num2[length_num2 - 1 - i]) - ord("0")
            t = x + add
            add = t // 10
            ans = str(t % 10) + ans
            i += 1

        if add:
            ans = str(add) + ans

        return ans