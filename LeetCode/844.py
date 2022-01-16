def makeString(text: str) -> dict:
        answer = []
        for i in text :
            if i != "#" : answer.append(i)
            else : 
                try: answer.pop()
                except: pass
        return answer

class Solution:

    def backspaceCompare(self, s: str, t: str) -> bool:
        answer_s = makeString(s)
        answer_t = makeString(t)

        return answer_t == answer_s