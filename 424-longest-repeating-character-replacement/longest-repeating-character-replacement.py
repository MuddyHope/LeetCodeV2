class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        

        # window len - count[max_frequency_letter of window] <= k

        count = {}

        left = 0
        res = 0

        for right in range(len(s)):
            # increment the counter
            count[s[right]] = 1 + count.get(s[right], 0)

            while (right - left + 1) - max(count.values()) > k:
                count[s[left]] -= 1
                left += 1

            res = max(res, right - left + 1)
        return res