def right(s):
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

def flip(i):
    answer = ''
    for j in i :
        if j == "(" :
            answer += ")"
        else :
            answer += "("
    return answer

def solution(p):
    answer = ''
    u = ''
    v = ''
    if right(p) == True :
        answer = p
    else :
        rights = 0
        lefts = 0
        for i in range(0,len(p),1) :
            if p[i] == "(" :
                rights += 1
            else :
                lefts += 1
            if rights == lefts :
                u = p[0:i+1]
                v = p[i+1:]
                if right(u) == True :
                    answer += (u+solution(v))
                    return answer
                else :
                    answer += "("+solution(v)+")"+flip(u[1:len(u)-1])
                    return answer
    return answer

print(solution("()))((()"))