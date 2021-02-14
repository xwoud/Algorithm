def solution(msg):
    referee = []
    answer = []
    msg = list(msg)
    rule = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']

    while msg :
        referee.append(msg.pop(0))
        while referee :
            if ''.join(referee) in rule :
                if len(msg) > 0 :
                    referee.append(msg.pop(0))
                else :
                    answer.append(rule.index(''.join(referee)) + 1)
                    break
            else :
                rule.append(''.join(referee))
                msg.insert(0,referee.pop(-1))
                answer.append(rule.index(''.join(referee)) + 1)
                referee = []
    return answer
