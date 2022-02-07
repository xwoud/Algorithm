class Solution:
    def reverseOnlyLetters(self, s: str) -> str:
        a, b=[], {}

        for i in range(len(s)):
            if s[i].isalpha():
                a.append(s[i])
            else:
                b[i]=s[i]
        a=a[::-1]

        for i in b:
            a.insert(i,b[i])
        return ''.join(a)