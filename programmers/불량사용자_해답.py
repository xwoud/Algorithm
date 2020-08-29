import re
from copy import deepcopy
check = []
def dfs_check(idx, candidates, arr, length):
    global answer,check
    if idx == len(candidates):
        if len(arr) == length and arr not in check:
            check.append(deepcopy(arr))
        return

    for each_id in candidates[idx] :
        if each_id not in arr:
            arr.add(each_id)
            dfs_check(idx+1,candidates,arr,length)
            arr.remove(each_id)

def solution(user_id, banned_id):
    candidates = []

    for i in range(len(banned_id)):
        banned_id[i] = re.compile("^"+banned_id[i].replace("*","([0-9]|[a-z])")+"$")
        temp = set()
        for each_user in user_id:
            if banned_id[i].match(each_user):
                temp.add(each_user)
        candidates.append(temp)
    dfs_check(0,candidates,set(),len(banned_id))
    return len(check)