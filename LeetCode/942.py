from typing import List

class Solution:
    def diStringMatch(self, s: str) -> List[int]:
        answer = []
        i,d = 0, len(s)
        for x in range(len(s)):
            if s[x] == "I":
                answer.append(i)
                i += 1
            elif s[x] == "D":
                answer.append(d)
                d -= 1
        
        if s[-1] == "I": answer.append(answer[-1]+1)
        else : answer.append(answer[-1]-1)

        return answer