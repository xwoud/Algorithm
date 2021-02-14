import re

def solution(files):
    lists = []
    answer = []

    for i in files:
        lists.append(re.split("([0-9]+)",i))

    my = sorted(lists, key = lambda x: (x[0].lower(), int(x[1])))

    for j in my :
        answer.append("".join(j))

    return answer
