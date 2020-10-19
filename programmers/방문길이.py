def solution(dirs):
    road = []
    now = [0,0]
    next = [0,0]

    for d in dirs:
        if (d == "U") and now[1] < 5 :
            next = [now[0],now[1]+1]
        elif (d == "D") and now[1] > -5 :
            next = [now[0],now[1]-1]
        elif (d == "R") and now[0] < 5 :
            next = [now[0]+1,now[1]]
        elif (d == "L") and now[0] > -5 :
            next = [now[0]-1,now[1]]
        if ([now,next] not in road) and ([next,now] not in road) and (next != now) :
            road.append([now,next])

        now = next

    return len(road)