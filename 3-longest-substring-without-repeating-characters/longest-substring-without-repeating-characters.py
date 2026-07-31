class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        i, j = 0, 1
        if not s:
            return 0
        if len(s) == 1:
            return 1
        max_res = 0
        seen = set()
        
        seen.add(s[i])
        while j < len(s):
            while s[j] in seen:
                seen.remove(s[i])
                i += 1
            seen.add(s[j])
            max_res = max(max_res, j - i + 1)
            j += 1
        return max_res

