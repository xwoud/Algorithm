def solution(skill, skill_trees):
    answer = 0

    for i in range(0,len(skill_trees),1):
        skill_trees[i] = ''.join(c for c in skill_trees[i] if c in skill)

    for k in skill_trees:
        if k == skill[0:len(k)] :
            answer +=1

    return answer