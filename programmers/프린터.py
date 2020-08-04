def solution(priorities, location):
    answer = 0
    location_stack = []
    priorities_copy = [[False] * 2 for i in range(len(priorities))]
    for i in range(0,len(priorities),1):
        priorities_copy[i][0] = priorities[i]
    priorities_copy[location][1] = True

    while(priorities_copy) :
        maxs = max(priorities_copy)[0]
        if priorities_copy[0][0] < maxs :
            priorities_copy.append(priorities_copy[0])
            priorities_copy.pop(0)
        else :
            location_stack.append(priorities_copy[0])
            priorities_copy.pop(0)

    for i in range(0,len(location_stack),1):
        if location_stack[i][1] == True:
            answer = i+1
            
    return answer
