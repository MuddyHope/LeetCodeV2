class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        
        hash_set = set()

        i, j = 0, 0
        max_length = 0

        for j in range(len(s)):
            while s[j] in hash_set:
                hash_set.remove(s[i])
                i += 1
            hash_set.add(s[j])
            max_length = max(max_length, j-i+1)
            j += 1
        return max_length
