class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        my_dict = {}
        left = 0
        res = 0
        for right in range(len(s)):
            my_dict[s[right]] = 1 + my_dict.get(s[right], 0)

            while (right - left + 1) - max(my_dict.values()) > k:
                my_dict[s[left]] -= 1
                left += 1
            res = max(res, right-left+1)
        return res
        