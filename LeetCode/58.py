class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        new_string = s.split()
        if new_string == [] :
            return 0
        else: return len(new_string[-1])


my = Solution()
print(my.lengthOfLastWord(" "))