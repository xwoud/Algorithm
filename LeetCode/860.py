from typing import List
from collections import Counter

class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        answer = Counter()
        for bill in bills:
            if bill != 5 :
                change = bill - 5
                if answer[change] > 0 : # 거스름돈 바로 있어면 줘버리기
                    answer[change] -= 1
                    answer[bill] += 1
                else : # 거스름돈 바로 없으면?
                    if change == 15:
                        if answer[10] > 0 and answer[5] > 0 :
                            answer[10] -= 1
                            answer[5] -= 1
                            answer[change+5] += 1
                        elif answer[5] >= 3:
                            answer[5] -= 3
                            answer[change+5] += 1
                        else :
                            return False
                    elif change == 10 :
                        if answer[10] > 0:
                            answer[10] -= 1
                            answer[change+5] += 1
                        elif answer[5] >= 2:
                            answer[5] -= 2
                            answer[change+5] += 1
                        else :
                            return False
                    elif change == 5:
                        return False

            else : 
                answer[5] += 1

        return True

mini = Solution()
print(mini.lemonadeChange([10,10]))