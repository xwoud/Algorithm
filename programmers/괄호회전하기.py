def isFair(s):
    if s%2 != 0 :
        return False
    stack = []
    for ch in s:
        if ch == "(" or ch == "[" or ch == "{":
            stack.append(ch)
        else:
            if len(stack) == 0:
                return False
            else :
                a = stack.pop()
                mini = a+ch
                if mini != "[]" and mini != "()" and mini != "{}":
                    return False
    return True

def solution(s):
    answer = 0
    for _ in range(len(s)):
        if isFair(s) :
            answer += 1
        s = s[1:]+s[0]

    return answer

print(solution("({)}"))