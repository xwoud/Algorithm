def solution(new_id):
    answer = ''
    new_id = new_id.lower()

    for i in new_id:
        if i.isalnum() or i in '-_.':
            answer += i

    while '..' in answer :
        answer = answer.replace('..', '.')

    if len(answer) > 0 and answer[0] == '.' : answer = answer[1:]
    if len(answer) > 0 and answer[-1] == '.' : answer = answer[:-1]

    if answer == '' : answer = 'a'

    if len(answer) >= 16 :
        answer = answer[:15]
        if answer[-1] == '.' : answer = answer[:-1]

    if len(answer) <= 3 :
        answer += answer[-1] * (3 - len(answer))

    return answer

print(solution("123_.def"))