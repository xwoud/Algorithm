from typing import List

class Solution:
    def minDeletionSize(self, strs: List[str]) -> int:
        delete = 0 
        for i in range(len(strs[0])):
            temp_col_str = ""
            for str in strs:
                if temp_col_str != "" and temp_col_str[-1] > str[i]:
                   delete += 1
                   break
                else:
                   temp_col_str += str[i]
            
        return delete