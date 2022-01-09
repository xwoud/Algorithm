def solution(k, dungeons):
    from itertools import permutations
    
    dungeons = list(permutations(dungeons, len(dungeons))) 
    dungeonNum = [] 
    
    cnt = 0 
    for dungeon in dungeons :
        fatigue = k
        for needFatigue, useFatigue in dungeon :
            if fatigue >= needFatigue : 
                fatigue -= useFatigue 
                cnt += 1
            else : break 
        dungeonNum.append(cnt)
        cnt = 0
    
    return max(dungeonNum)