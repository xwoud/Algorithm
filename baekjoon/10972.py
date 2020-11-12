from __future__ import print_function
import sys

n = int(sys.stdin.readline())
k = 0
num_list = list(map(int, sys.stdin.readline().split()))
for i in range(n-1,0,-1):
    j = i - 1
    if num_list[i] > num_list[j] :
        k = 1
        if i == len(num_list)-1 :
            num_list[i],num_list[j] = num_list[j],num_list[i]
            break
        else :
            re_list = num_list[j:]
            num_list = num_list[:j]
            i = 0
            j = len(re_list)-1
            while re_list[i] >= re_list[j]:
                j -= 1
            re_list[i], re_list[j] = re_list[j], re_list[i]
            h = 1
            t = len(re_list)-1
            while h<t:
                re_list[h],re_list[t] = re_list[t],re_list[h]
                t -= 1
                h += 1
            num_list = num_list + re_list
            break

if k == 0 :
    print('-1')
else :
    for i in num_list:
        print(i, end=' ')
# import sys
# import itertools
#
# n = int(sys.stdin.readline())
# now_arr = tuple(map(int, sys.stdin.readline().split()))
# nPr = list(itertools.permutations(list(range(1, n+1)), n))
# if now_arr == nPr[-1] :
#     print(-1)
# else :
#     for i in nPr[list(nPr).index(now_arr) + 1]:
#         print(i,end = " ")
