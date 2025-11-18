class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        
        i, j = 0, 0
        hash_map = {}
        max_length = 0

        while j < len(s):
            # If char already exists in window, move left pointer
            if s[j] in hash_map and hash_map[s[j]] >= i:
                i = hash_map[s[j]] + 1   # shrink window properly

            # Update latest index of character
            hash_map[s[j]] = j

            # Update max length using window size
            max_length = max(max_length, j - i + 1)

            j += 1

        return max_length
