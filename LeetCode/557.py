class Solution:

    def reverseWord(self,word):
        end = len(word)-1
        answer = ""

        while(end >= 0):
            answer += word[end]
            end = end-1
        return answer

    def reverseWords(self, s: str) -> str:
        answer = ""
        word = ""
        i = 0

        while(i <= len(s)-1):
            if (s[i] != " "):
                word += s[i]
            else:
                answer += self.reverseWord(word) + " "
                word = ""
            i = i+1

        answer += self.reverseWord(word)
        return answer
