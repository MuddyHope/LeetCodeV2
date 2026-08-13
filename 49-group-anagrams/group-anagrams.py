class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        res = defaultdict(list)
        for word in strs:
            temp = [0] * 26

            for letter in word:
                temp[ord(letter) - ord('a')] += 1
            res[tuple(temp)].append(word)
        return list(res.values())