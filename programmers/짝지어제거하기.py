def solution(s):
    
    stacks = []
    for i in s:
        if len(stacks) > 0:
            if stacks[-1] == i:
                stacks.pop()
            else:
                stacks.append(i)
        else:
            stacks.append(i)

    if stacks :
        return 0
    else :
        return 1
