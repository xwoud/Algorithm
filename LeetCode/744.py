class Solution:
    def nextGreatestLetter(self, letters: list[str], target: str) -> str:
        answer = 123
        target = ord(target)
        for i in range(0, len(letters),1):
            letters[i] = ord(letters[i])
            if (letters[i] > target) and (letters[i] < answer):
                answer = letters[i]

        if answer != 123 :
            answer = chr(answer)
        else :
            answer = chr(min(letters))

        return answer
