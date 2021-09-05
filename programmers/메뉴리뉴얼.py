from itertools import combinations
from collections import Counter

def solution(orders, course):
    
    answer = []
    for i in course:
        number = []
        for j in orders:
            number += list(map(''.join, combinations(sorted(j), i)))
        for a,b in Counter(number).most_common():
            if b == max(Counter(number).values()) and max(Counter(number).values()) > 1:
                answer.append(a)
    answer.sort()
    
    return answer
