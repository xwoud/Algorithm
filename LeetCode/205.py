class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        L = list(zip(s, t))
        M = []
        N = []
        for i in set(L):
            M.append(i[0])
            N.append(i[1])
        if len(M) > len(set(M)) or len(N) > len(set(N)):
            return False
        else:
            return True

my = Solution()
print(my.isIsomorphic("foo","bar"))