def dfs(shot, apeach_board, idx, apeach_score, lion_score, lion_board): 

    if shot == 0: 
        global max_val, answer
        if lion_score - apeach_score > max_val:
            max_val = lion_score - apeach_score 
            answer = lion_board[:] 

        elif lion_score - apeach_score == max_val and max_val != 0:
            for i in range(10, -1, -1): 
                if lion_board[i] > answer[i]:
                    answer = lion_board[:]
                    break
                elif lion_board[i] < answer[i]: 
                    break
        return

    for i in range(idx, 11):
        if shot > apeach_board[i]:
            lion_board[i] = apeach_board[i] + 1
            if apeach_board[i] > 0:
                dfs(shot - lion_board[i], apeach_board, i + 1, apeach_score - (10 - i), lion_score + (10 - i), lion_board)
            else: 
                dfs(shot - lion_board[i], apeach_board, i + 1, apeach_score, lion_score + (10 - i), lion_board)
            lion_board[i] = 0
        else: 
            if i == 10:
                lion_board[i] = shot 
                dfs(0, apeach_board, i + 1, apeach_score, lion_score, lion_board)
                lion_board[i] = 0
            else:
                dfs(shot, apeach_board, i + 1, apeach_score, lion_score, lion_board)


def solution(n, info):
    global max_val, answer
    apeach_score = 0
    answer = [0 for _ in range(11)]
    max_val = 0

    for i in range(11):
        if info[i] > 0:
            apeach_score += 10 - i
    dfs(n, info, 0, apeach_score, 0, [0 for _ in range(11)])

    if answer == [0 for _ in range(11)]:
        answer = [-1]
    return answer