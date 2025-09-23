from collections import defaultdict
from typing import List

class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        indegree = [0] * (n + 1)   # how many people trust them
        outdegree = [0] * (n + 1)  # how many they trust

        for a, b in trust:
            outdegree[a] += 1
            indegree[b] += 1

        print(outdegree)
        print(indegree)

        for person in range(1, n + 1):
            if indegree[person] == n - 1 and outdegree[person] == 0:
                return person
        return -1
