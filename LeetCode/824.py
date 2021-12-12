class Solution:
    def toGoatLatin(self, sentence: str) -> str:
        vowel = ("a", "A", "e", "E", "i", "I", "o", "O", "u", "U")
        sentence = sentence.split(" ")
        answer = []

        for i in sentence:
            if i.startswith(vowel):
                answer.append(i+"ma")
            else :
                answer.append(i[1:]+i[0]+"ma")

        for i in range(len(answer)):
            answer[i] += 'a' * (i+1)
        return ' '.join(answer)
