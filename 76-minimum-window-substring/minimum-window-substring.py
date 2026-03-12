from collections import Counter

class Solution:
    def minWindow(self, s: str, t: str):

        res = ""
        min_length = float("inf")

        if len(t) > len(s):
            return res

        t_dict = Counter(t)
        s_dict = {}

        left = 0

        for right in range(len(s)):

            s_dict[s[right]] = 1 + s_dict.get(s[right], 0)

            # check if window satisfies t
            valid = True
            for c in t_dict:
                if s_dict.get(c, 0) < t_dict[c]:
                    valid = False
                    break

            while valid:

                if (right - left + 1) < min_length:
                    min_length = right - left + 1
                    res = s[left:right+1]

                # shrink window
                s_dict[s[left]] -= 1
                if s_dict[s[left]] == 0:
                    del s_dict[s[left]]

                left += 1

                # check validity again
                valid = True
                for c in t_dict:
                    if s_dict.get(c, 0) < t_dict[c]:
                        valid = False
                        break

        return res