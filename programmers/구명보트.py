def solution(people, limit):
    answer = 0
    people.sort(reverse=True)
    first = 0
    second = len(people)-1
    while first <= second :
        if people[first] + people[second] <= limit:
            second -= 1
        answer += 1
        first += 1

    return answer

print(solution([70, 80, 50],100))