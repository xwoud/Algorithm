def change(number,base):
    noti = "0123456789ABCDEF"
    q,r = divmod(number,base)
    n = noti[r]
    return change(q, base) + n if q else n

def solution(n):
    answer = str(change(n,3))[::-1]
    answer = int(answer,3)
    return answer