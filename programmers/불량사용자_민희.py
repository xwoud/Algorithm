import re

def solution(user_id, banned_id):
    answer_count = []
    answer = 1
    for i in range(len(banned_id)):
        count = 0
        banned_id[i] = re.compile("^"+banned_id[i].replace("*","([0-9]|[a-z])")+"$")
        for j in user_id:
            if banned_id[i].match(j):
                count += 1
        answer_count.append(count)

    for k in answer_count :
        answer *= k

    return answer

print(solution(["frodo", "fradi", "crodo", "abc123", "frodoc"],["fr*d*", "*rodo", "******", "******"]))