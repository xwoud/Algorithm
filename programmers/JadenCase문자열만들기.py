def solution(s):
    s = s.lower()
    answer = ""
    for i in s.split(" "):
        i = i.capitalize()
        answer += i + " "
    return answer[:-1]