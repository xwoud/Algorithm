from __future__ import print_function
import sys

N = int(input())
arr = []
lists = []
for i in range(N):
    a = str(sys.stdin.readline().rstrip())
    lists = a.split()
    if lists[0] == "add":
        if lists[1] not in arr:
            arr.append(lists[1])
    elif lists[0] == "remove":
        if lists[1] in arr:
            arr.remove(lists[1])
    elif lists[0] == "check":
        if lists[1] in arr:
            print("1")
        else :
            print("0")
    elif lists[0] == "toggle":
        if lists[1] in arr:
            arr.remove(lists[1])
        else :
            arr.append(lists[1])
    elif lists[0] == "all":
        arr = ['1','2','3','4','5','6','7','8','9','10','11','12','13','14','15','16','17','18','19','20']
    elif lists[0] == "empty":
        arr = []
