def solution(n, arr1, arr2):
    answer = []

    for i in range(0,n,1):
        k = bin(arr1[i]|arr2[i])[2:]
        if len(k) != n :
            k = (n-len(k))*"0" + k
        k = k.replace('1','#')
        k = k.replace('0', ' ')
        answer.append(k)

    return answer