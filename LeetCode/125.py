import re

class Solution:
    def isPalindrome(self, s: str) -> bool:

        new_string = re.sub(r"[^a-zA-Z0-9]","",s)
        new_string = new_string.lower()
        if new_string == new_string[::-1] :
            return True
        else :
            return False


my = Solution()
print(my.isPalindrome("A man, a plan, a canal: Panama"))