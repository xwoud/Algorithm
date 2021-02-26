def changeTime(time):
    k = 0
    result = 0
    for i in time:
        if k == 0 :
            result += int(i) * 3600
        if k == 1 :
            result += int(i) * 60
        if k == 2 :
            result += int(i)
        k += 1
    return result

def solution(play_time, adv_time, logs):
    answer = ''

    logs_start_sec = []
    logs_end_sec = []

    play_time_sec = changeTime(play_time.split(":"))
    adv_time_sec = changeTime(adv_time.split(":"))

    total_time = [0 for col in range(play_time_sec)]

    for i in logs:
        start = True
        for j in i.split("-"):
            if start == True :
                logs_start_sec.append(changeTime(j.split(":")))
            else :
                logs_end_sec.append(changeTime(j.split(":")))
            start = False
    for i in range(len(logs)):
        total_time[logs_start_sec[i]] += 1
        total_time[logs_end_sec[i]] -= 1

    for i in range(1,play_time_sec-1,1):
        total_time[i] += total_time[i - 1]

    for i in range(1,play_time_sec-1,1):
        total_time[i] += total_time[i - 1]

    for i in range(adv_time_sec-1,play_time_sec-1,1):
        


    return answer

print(solution("02:03:55","00:14:15",["01:20:15-01:45:14", "00:40:31-01:00:00", "00:25:50-00:48:29", "01:30:59-01:53:29", "01:37:44-02:02:30"]))