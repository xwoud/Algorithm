import sys

sevenList = []
for _ in range(9): sevenList.append(int(sys.stdin.readline()))

maxs = sum(sevenList)

while len(sevenList) != 7 :
    fakeOne = sevenList.pop(0)
    fakeTwo = maxs - 100 - fakeOne
    if fakeTwo in sevenList :
        sevenList.remove(fakeTwo)
    else :
        sevenList.append(fakeOne)

sevenList.sort()

for i in sevenList: print(i)
