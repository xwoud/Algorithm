def solution(record):
    answer = []
    user = {}
    for i in record:
        if i.split(' ')[0] != 'Leave' :
            user[i.split(' ')[1]] = i.split(' ')[2]
    for j in record:
        if j.split(' ')[0] == 'Enter' :
            nick = user[j.split(' ')[1]]
            answer.append(nick+"님이 들어왔습니다.")
        elif j.split(' ')[0] == 'Leave' :
            nick = user[j.split(' ')[1]]
            answer.append(nick + "님이 나갔습니다.")

    return answer
