class Solution:

    def buddyStrings(self, s: str, goal: str) -> bool:
        if len(s) != len(goal):
            return False
        
        ans = False
        second = False
        double = False
        
        if len(s) != len(set(s)) and Counter(s) == Counter(goal):
            double = True
            
        j = -1

        for i in range(len(s)):
            if s[i] != goal[i]: 
                if j < 0: 
                    j = i
                elif ans: 
                    second = True 
                    break
                else:
                    if s[i] == goal[j] and s[j] == goal[i]: 
                        ans = True 
                    else: 
                        second = True
                        break
        
        return (ans or double) and not second

    ''' 
    Run Time Error 난 코드 
    def buddyStrings(self, s: str, goal: str) -> bool:

        if len(s) != len(goal):
            return False

        if s == goal:
            return len(set(s)) < len(goal)

        diffs, goals = [], []
        for i,j in s, goal:
            if i != j : 
                diffs.append(i)
                goals.append(j)
        
        if len(diffs) != 2 :
            return False

        return diffs[0] == goals[1] and diffs[1] == goals[0]
    '''