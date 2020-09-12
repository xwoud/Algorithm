# -*- coding: utf-8 -*-
import re
from itertools import permutations

def solution(expression):

    op = [list(y) for y in permutations(['*','+','-'])]
    ex = re.split('(\D)',expression)

    a = []
    for x in op:
        copyex = ex[:]
        for y in x:
            while y in copyex:
                tmp = copyex.index(y)
                copyex[tmp-1] = str(eval(copyex[tmp-1]+copyex[tmp]+copyex[tmp+1]))
                copyex = copyex[:tmp]+copyex[tmp+2:]
        a.append(copyex[-1])

    answer = 0
    for i in a :
        if answer < abs(int(i)) :
            answer = abs(int(i))
    return answer

