from __future__ import print_function
import sys

n,m = map(int, sys.stdin.readline().split())
num_list = list(map(int, sys.stdin.readline().split()))
sum_numbers = [0 for _ in range(n)]
for i in range(n):
    if i == 0:
        sum_numbers[i] = num_list[i]
    else:
        sum_numbers[i] = sum_numbers[i-1] + num_list[i]

for _ in range(m):
    i, j = map(int, sys.stdin.readline().split())
    if i == 1:
        print(sum_numbers[j-1])
    else:
        print(sum_numbers[j-1] - sum_numbers[i-2])