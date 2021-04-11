import itertools

while True:
    item = list(map(int, input().split()))

    if item[0] == 0 :
        break

    item = item[1:]

    for i in list(itertools.combinations(item,6)):
        for j in i : print(j, end = " ")
        print()
    print()
