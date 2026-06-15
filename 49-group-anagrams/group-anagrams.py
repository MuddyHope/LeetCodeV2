class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        res = []
        hash_map = defaultdict(list)

        for word in strs:
            word_map = [0] * 26
            for letter in word:
                word_map[ord(letter) - ord('a')] += 1
            hash_map[tuple(word_map)].append(word)
        
        return list(hash_map.values())