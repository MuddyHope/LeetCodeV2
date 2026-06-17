class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        
        i, j = 0, 0
        max_len = 0
        hash_map = {}

        while j < len(s):
            hash_map[s[j]] = hash_map.get(s[j], 0) + 1
            while hash_map[s[j]] > 1:
                hash_map[s[i]] -= 1 
                i += 1
            max_len = max(max_len, j-i + 1)

            j += 1
        return max_len
            
