from typing import List
from collections import Counter


class Solution:
    def mostCommonWord(self, paragraph: str, banned: List[str]) -> str:
        words = ''.join([word.lower() if word.isalnum() == True else ' ' for word in paragraph])
        dictToWords = dict(Counter(words.split()))
        
        for ban in banned:
            if ban in dictToWords.keys():
                del dictToWords[ban]
        return max(dictToWords,key = lambda x:dictToWords[x])