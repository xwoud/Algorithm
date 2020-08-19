def solution(number, k):
    list_k = []
    for i, j in enumerate(number):
        while len(list_k) > 0 and list_k[-1] < j and k > 0:
            list_k.pop()
            k -= 1
        list_k.append(j)
    if k!=0:
        list_k = list_k[:-k]
    answer = ''.join(list_k)

    return answer
