class Solution:
    def detectCapitalUse(self, word: str) -> bool:
        if word.lower() == word or word.upper() == word or word.title() == word:
            return True
        else:
            return False