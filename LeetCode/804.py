from typing import List


class Solution:
    def uniqueMorseRepresentations(self, words: List[str]) -> int:
        mos = [".-","-...","-.-.","-..",".","..-.","--.","....","..",".---","-.-",".-..","--","-.","---",".--.","--.-",".-.","...","-","..-","...-",".--","-..-","-.--","--.."]
        answerArray = set()
        for i in words:
            chageMos = []
            for j in i:
                chageMos+=[mos[ord(j)-ord('a')]]
            answerArray.add("".join(chageMos))
        return len(answerArray)