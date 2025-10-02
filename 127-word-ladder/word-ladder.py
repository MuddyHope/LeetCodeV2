from collections import deque

class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: list[str]) -> int:
        if endWord not in wordList:
            return 0
        
        # BFS
        q = deque([(beginWord, 1)])
        visited = set([beginWord])
        
        while q:
            word, length = q.popleft()
            if word == endWord:
                return length
            
            for nxt in wordList:
                if nxt not in visited and self.is_one_diff(word, nxt):
                    visited.add(nxt)
                    q.append((nxt, length + 1))
        
        return 0

    def is_one_diff(self, w1: str, w2: str) -> bool:
        diff = 0
        for a, b in zip(w1, w2):
            if a != b:
                diff += 1
                if diff > 1:  # exactly one position must differ
                    return False
        return diff == 1
