class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        my_set = set()
        left, right = 0, 0
        max_string = 0

        while right < len(s):
            if s[right] in my_set:
                my_set.remove(s[left])
                left += 1
            else:
                my_set.add(s[right])
                max_string = max(max_string, right - left + 1)
                right += 1

        return max_string

            