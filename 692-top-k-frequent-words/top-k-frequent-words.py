class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        counter = defaultdict(set)

        for word in set(words):
            freq = words.count(word)
            counter[freq].add(word)

        res = []

        for freq in range(len(words), 0, -1):
            if freq in counter:
                for word in sorted(counter[freq]):
                    res.append(word)

                    if len(res) == k:
                        return res

        return res