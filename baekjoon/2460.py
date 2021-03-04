import sys

# 비교를 이용한 풀이
answer = 0
maxPeople = 0
for _ in range(10):
    n, m = map(int, sys.stdin.readline().split())
    answer += m - n
    if answer > maxPeople :
        maxPeople = answer

print(maxPeople)

# 배열을 이용한 풀이
# answer = 0
# answerList = []
# for _ in range(10):
#     n, m = map(int, sys.stdin.readline().split())
#     answer += (m - n)
#     answerList.append(answer)
#
# print(max(answerList))
