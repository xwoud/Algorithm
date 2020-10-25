# -*- coding: utf-8 -*-
def change(number,base):
    noti = "0123456789ABCDEF"
    q,r = divmod(number,base)
    n = noti[r]
    return change(q, base) + n if q else n

def solution(n, t, m, p):
    answer = []
    changeNum = []
    for i in range(0,t*m,1):
        changeNum.append(change(i,n))
    text = "".join(changeNum)
    i = 0
    while(len(answer) < t):
        answer.append(text[i:i + m][p - 1])
        i = i + m
    return "".join(answer)