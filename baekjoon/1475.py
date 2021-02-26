from __future__ import print_function

n = list(map(int, str(input())))

num_set = {0: 0, 1: 0, 2: 0, 3: 0, 4: 0, 5: 0, 6: 0, 7: 0, 8: 0, 9: 0}

for i in n:
    if i == 9:
        num_set[6] += 1
    else :
        num_set[i] += 1

if num_set[6] % 2 == 1:
    num_set[6] = num_set[6] // 2 + 1
else :
    num_set[6] = num_set[6] // 2

print(max(num_set.values()))