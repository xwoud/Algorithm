class Solution:
    def findRelativeRanks(self, score: list[int]) -> list[str]:
        myDict = {}
        myList = sorted(score, reverse=True)

        for i in range(0, len(myList)):
            if i == 0:
                myDict[myList[i]] = 'Gold Medal'
            elif i == 1:
                myDict[myList[i]] = 'Silver Medal'
            elif i == 2:
                myDict[myList[i]] = 'Bronze Medal'
            else:
                myDict[myList[i]] = str(i + 1)
        ret = []

        for i in range(0, len(score)):
            ret.append(myDict[score[i]])

        return ret