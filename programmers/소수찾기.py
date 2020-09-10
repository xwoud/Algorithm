from itertools import permutations

def is_prime(num):
    if num <= 1:
        return False
    for i in range(2, num):
        if num % i == 0:
            return False
    return True

def solution(numbers):
    my = []
    new = []
    mylist = list(numbers)
    for i in range(1,len(numbers)+1,1):
        my.append(map(''.join,permutations(mylist,i)))
    for j in my:
        for k in j:
            if k[0] != '0' :
                if is_prime(int(k)) == True :
                    new.append(int(k))

    new_list = []
    for v in new:
        if v not in new_list:
            new_list.append(v)

    return len(new_list)
