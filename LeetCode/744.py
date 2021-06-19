class Solution:
    def nextGreatestLetter(self, letters: list[str], target: str) -> str:
        answer = 123
        target = ord(target) - 96
        for i in range(0, len(letters), 1):
            letters[i] = ord(letters[i]) - 96
            if (letters[i] > target) and (letters[i] < answer):
                answer = letters[i]

        if answer != 123:
            answer = chr(answer + 96)
        else:
            answer = chr(min(letters) + 96)

        return answer
