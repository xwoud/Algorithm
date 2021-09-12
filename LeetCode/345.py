class Solution:
    def reverseVowels(self, s: str) -> str:
        vowels = ["a","e","o","u","i","A","E","O","U","I"]
        vowelsList = list(filter(lambda x: x in vowels, s))
        answer = list(map(lambda x: vowelsList.pop() if x in vowels else x, s))

        return "".join(answer)