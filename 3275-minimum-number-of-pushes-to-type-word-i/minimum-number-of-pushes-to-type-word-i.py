from collections import Counter

class Solution:
    def minimumPushes(self, word: str) -> int:
        
        res = 0
        pushes = 1

        for i in range(1, len(word)+1):
            res += pushes

            if (i%8) == 0:
                pushes += 1
        return res
