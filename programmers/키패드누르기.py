def solution(numbers, hand):
    key = [[1, 2, 3], [4, 5, 6], [7, 8, 9], ['*', 0, '#']]
    answer = ''
    L = [3, 0]
    R = [3, 2]
    for i in numbers:
        if i == 1 or i == 4 or i == 7 :
            answer+='L'
            for j in range(0,len(key),1):
                    if key[j][0] == i :
                        L = [j,0]
                        break
        elif i == 3 or i == 6 or i == 9 :
            answer+='R'
            for j in range(0, len(key), 1):
                if key[j][2] == i:
                    R = [j, 0]
                    break
        else :
            for j in range(0,len(key),1):
                for k in range(0,3,1):
                    if key[j][k] == i :
                        L_index = abs(L[0] - j) + abs(L[1] - k)
                        R_index = abs(R[0] - j) + abs(R[1] - k)
                        if L_index < R_index:
                            answer+='L'
                            L = [j,k]
                        elif L_index > R_index:
                            answer+='R'
                            R = [j, k]
                        else :
                            if hand == "right" :
                                answer+='R'
                                R = [j, k]
                            else :
                                answer+='L'
                                L = [j, k]
                        break

    return answer
