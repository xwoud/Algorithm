def solution(operations):
    que = []
    answer = []
    for i in operations:
        if i[0] == "I" :
            que.append(int(i[2:]))
        elif i == "D 1":
            if len(que) != 0 :
                print("hi:",max(que))
                que.remove(max(que))
        else :
            if len(que) != 0:
                que.remove(min(que))
        print(que)
    if len(que)==0 :
        answer = [0,0]
    else :
        answer = [max(que),min(que)]
    return print(answer)
