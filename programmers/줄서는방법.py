def factorial(n):
    if n == 1:
        return 1
    return n * factorial(n - 1)

def solution(n, k):
    answer = []
    exList = [i for i in range(1, n + 1)]

    while (n != 0):

        temp = factorial(n) // n
        index = k // temp
        k = k % temp

        if k == 0:
            answer.append(exList.pop(index - 1))
        else:
            answer.append(exList.pop(index))
        n -= 1

    return answer