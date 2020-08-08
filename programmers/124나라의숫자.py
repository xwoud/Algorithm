def solution(n):
    answer = ''
    while n:
        n -= 1
        if n%3 == 0 :
            answer = '1' + answer
        elif n%3 == 1 :
            answer = '2' + answer
        elif n%3 == 2 :
            answer = '4' + answer
        n //= 3
    return answer