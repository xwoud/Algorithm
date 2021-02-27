import sys

N = int(sys.stdin.readline())
r_answer = list(map(int, input().split()))
M = int(sys.stdin.readline())

start = 0
end = max(r_answer)

while start <= end:
    mid = (start+end)//2
    total = 0

    for i in r_answer:
        total += min(mid , i)

    if total <= M :
        start = mid + 1
    else :
        end = mid - 1

print(end)



# import sys
#
# N = int(sys.stdin.readline())
# r_answer = list(map(int, input().split()))
# M = int(sys.stdin.readline())
# answer = 0
#
# while (M >= N and N !=0):
#     k = M // N
#     answer += k
#     for i in range(len(r_answer)):
#         if r_answer[i] >= k:
#             M -= k
#             r_answer[i] -= k
#         elif r_answer[i] < k and r_answer[i] > 0 :
#             M -= r_answer[i]
#             r_answer[i] = 0
#     t = 0
#     for i in r_answer:
#         if i != 0 :
#             t += 1
#     N = t
#
# print(answer)