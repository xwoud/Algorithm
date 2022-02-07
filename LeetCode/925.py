class Solution:
    def isLongPressedName(self, name, typed):

        elementName = 0
        namePresent = 0
        countName = len(name)
        countType = len(typed)

        if name[0] != typed[0]:
            return False

        while elementName < countType:
            if namePresent < countName and name[namePresent] == typed[elementName]:
                namePresent +=1

            elif typed[elementName] != typed[elementName-1]:
                return False

            elementName +=1
        return namePresent == countName
