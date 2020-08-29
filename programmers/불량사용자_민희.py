import re

def solution(user_id, banned_id):
    answer_count = []
    for i in range(len(banned_id)):
        count = 0
        banned_id[i] = re.compile("^"+banned_id[i].replace("*","([0-9]|[a-z])")+"$")
        list = []
        for j in user_id:
            if banned_id[i].match(j):
                list.append(j)
        answer_count.append(list)

    match_list = []
    for k in range(len(answer_count[0])):
        if len(match_list) == 0 :
                match_list.append(answer_count[0][k])
        for i in range(1, len(answer_count), 1):
            for j in range(len(answer_count[i])):
                if answer_count[i][j] in match_list:
                    pass
                else:
                    match_list.append(answer_count[i][j])
                    break
        if len(match_list) == len(banned_id) :
            count += 1
        match_list = []
    return count

print(solution(["frodo", "fradi", "crodo", "abc123", "frodoc"],["fr*d*", "*rodo", "******", "******"]))
