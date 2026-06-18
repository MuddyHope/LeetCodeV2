class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        hash_map = defaultdict(list)
        counter = defaultdict(list)
        for word in strs:
            counter = [0] * 26
            for letter in word:
                counter[ord(letter) - ord('a')] += 1
            hash_map[tuple(counter)].append(word)
        
        return list(hash_map.values())