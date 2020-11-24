from __future__ import print_function
import sys

n,m = map(int, sys.stdin.readline().split())

first = 'a'
second = 'b'

while(n-2):
    first, second = second, first + second
    n -= 1

i = 1
state = False
while(True):
    j = 1
    while(True):
        check = second.count('a')*i + second.count('b')*j
        if check > m :
            break
        elif check == m :
            state = True
            break
        j += 1
    if state == True:
        break
    i += 1
print(i)
print(j)