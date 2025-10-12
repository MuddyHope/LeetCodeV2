from collections import Counter
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hash_map = defaultdict(list)


        for each in strs:
            D = [0] * 26
            for each_letter in each:
                D[ord(each_letter)-ord('a')] += 1
            hash_map[tuple(D)].append(each)
        
        res = hash_map.values()
        return (list(res))

    
        