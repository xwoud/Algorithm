from datetime import datetime

def replaceFunc(s):
    s = s.replace('A#', 'M')
    s = s.replace('F#', 'I')
    s = s.replace('C#', 'N')
    s = s.replace('D#', 'H')
    s = s.replace('G#', 'I')
    return s

def solution(m, musicinfos):
    m = replaceFunc(m)
    answer = []
    for i in musicinfos:
        start, end, title, melody = i.split(',')
        melody = replaceFunc(melody)

        time = str(datetime.strptime(end, '%H:%M') - datetime.strptime(start,'%H:%M')).split(':')
        totalTime = int(time[0])*60 + int(time[1]) # 분으로 환산

        totalMelody = melody * (totalTime // len(melody)) + melody[:(totalTime%len(melody))]

        if m in totalMelody:
            answer.append([title,totalTime])

    if len(answer) == 1 :
        return answer[0][0]
    elif len(answer) == 0 :
        return "(None)"
    else :
        answer = sorted(answer, key=(lambda x: int(-x[1])))
        return answer[0][0]
