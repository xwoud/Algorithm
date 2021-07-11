class Solution:
    def restoreString(self, s: str, indices: list[int]) -> str:
        mylist = [""] * len(s)
        i = 0
        for j in indices:
            mylist[j] = s[i]
            i += 1
        return "".join(mylist)

