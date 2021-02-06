from itertools import combinations

def solution(orders, course):
    answer = []
    numbers = [0]*10001
    print(numbers)
    for k in range(0,len(orders),1):
        for i in range(2, len(orders[k])):
            if answer not in combinations(orders[k], i):
                print(combinations(orders[k], i))
            # print(list(map(''.join, combinations(orders[k], i))))
    return answer

print(solution(["ABCFG", "AC", "CDE", "ACDE", "BCFG", "ACDEH"],[2,3,4]))