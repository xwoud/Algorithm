import sys
from collections import Counter

def mean(lists):
    return round(sum(lists)/len(lists))

def median(lists):
    lists.sort()
    return num_list[len(lists) // 2]


def mode(lists):
    mode_dict = Counter(lists)
    modes = mode_dict.most_common()

    if len(lists) > 1:
        if modes[0][1] == modes[1][1]:
            mod = modes[1][0]
        else:
            mod = modes[0][0]
    else:
        mod = modes[0][0]

    return mod

def scope(lists):
    return max(lists) - min(lists)

N = int(sys.stdin.readline())
num_list = list(map(int,(input() for _ in range(N))))

print(mean(num_list))
print(median(num_list))
print(mode(num_list))
print(scope(num_list))
