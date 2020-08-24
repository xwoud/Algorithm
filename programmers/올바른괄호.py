def solution(s):
    stack = []
    for i in s:
        if i == "(":
            stack.append(i)
        else:
            if len(stack) == 0:
                return False
                break
            else:
                stack.pop()
    answer = (len(stack) == 0)
    return answer