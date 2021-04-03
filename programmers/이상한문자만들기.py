def solution(s):
    answer = ''
    for name in s.split(" "):
        for a,b in enumerate(name):
            if a % 2 == 0 :
                answer += b.upper()
            else :
                answer += b.lower()
        answer += " "

    return answer[:-1]

print(solution("try hello world"))
