def solution(array, commands):
    answer1 = []
    answer2 = []
    for i in range(0, len(commands), 1):
        answer1 = array[commands[i][0] - 1:commands[i][1]]
        answer1.sort()
        answer2.insert(i, answer1[commands[i][2] - 1])

    return answer2
