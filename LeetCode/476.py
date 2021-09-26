class Solution:
    def findComplement(self, num: int) -> int:
        num = list(bin(num))[2:]
        for i,n in enumerate(num):
            num[i] = str(1-int(n))
        return int("".join(num),2)