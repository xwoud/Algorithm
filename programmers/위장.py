from collections import Counter

def solution(clothes):
    answer = 1
    category_count = Counter([i for _, i in clothes])

    for i in category_count :
        answer *= category_count[i]+1

    return answer-1
