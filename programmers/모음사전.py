from itertools import product

def solution(word):
    dict = []
    for i in range(1,6) :
        dict += list(map(''.join, product("AEIOU", repeat = i)))
        print(dict)
    dict.sort()
    
    answer = dict.index(word) + 1
    
    return answer

print(solution("AAAAE"))
