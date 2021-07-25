class Solution:
    def isValid(self, s: str) -> bool:

        answerStack = []
        answerDict = {')':'(', ']':'[', '}':'{'}

        for i in s:
            if i not in answerDict:
                # 열리는 괄호
                answerStack.append(i)
            elif not answerStack or answerStack.pop() != answerDict[i] :
                # 닫히는 괄호인데~ answerStack에 열리는 괄호가 없거나 있는데 마지막에 들어있는게 얘의 답이 아니라면?
                return False

        if answerStack : return False

        return True

my = Solution()
print(my.isValid("}"))