import collections
from typing import List

class Solution:
    def hasGroupsSizeX(self, deck: List[int]) -> bool:
        deckCounter = collections.Counter(deck).values()

        for i in range(2, max(deckCounter)+1):
            if all([not c % i for c in deckCounter]):
                return True
        return False