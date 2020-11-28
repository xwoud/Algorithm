from __future__ import print_function
import sys
from itertools import permutations

N = int(sys.stdin.readline())
arr = [i for i in range(1, N+1)]

for numbers in list(permutations(arr)):
    for num in numbers:
        print(num, end=' ')
    print()