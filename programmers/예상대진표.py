def solution(n,a,b):
    answer = 0
    while a != b:
        answer += 1
        a = (a+1)//2
        b = (b+1)//2
    return answer


print(solution(8,4,7))


# def solution(n, a, b):
#     member = list(range(1, n + 1))
#     winner = []
#     indexs = 1
#
#     while True:
#
#         for i in range(0, len(member), 2):
#             if member[i] == a and member[i + 1] == b:
#                 return indexs
#             elif member[i] == a or member[i] == b:
#                 winner.append(member[i])
#             elif member[i + 1] == a or member[i + 1] == b:
#                 winner.append(member[i + 1])
#             else:
#                 winner.append(member[i])
#
#         indexs += 1
#         member = winner
#         winner = []
#
#     return indexs
#
