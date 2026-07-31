class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        max_res = 0
        i, j = 0, 0

        seen = set()
        
        while j < len(s):
            while s[j] in seen:
                seen.remove(s[i])
                i += 1
            seen.add(s[j])
            max_res = max(max_res, j - i + 1)
            j += 1
        return max_res

