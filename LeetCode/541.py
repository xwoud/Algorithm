class Solution:
    def reverseStr(self, s: str, k: int) -> str:
        answer = ''
        for i in range(0, len(s), k):
            tmp = s[i: i + k]
            if (i // k) % 2 == 0:
                answer = answer + tmp[::-1]
            else:
                answer = answer + tmp
        return answer
