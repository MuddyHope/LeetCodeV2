from collections import Counter

class Solution:
    def minWindow(self, s: str, t: str) -> str:

        if len(s) < len(t):
            return ""

        t_counter = dict(Counter(t))
        s_counter = {}

        res = ""
        min_len = float("inf")

        i = 0
        j = 0

        while j < len(s):

            s_counter[s[j]] = 1 + s_counter.get(s[j], 0)

            valid = True

            for letter, count in t_counter.items():
                if s_counter.get(letter, 0) < count:
                    valid = False
                    break

            while valid:

                if (j - i + 1) < min_len:
                    min_len = j - i + 1
                    res = s[i:j+1]

                s_counter[s[i]] -= 1

                if s_counter[s[i]] == 0:
                    del s_counter[s[i]]

                i += 1

                valid = True

                for letter, count in t_counter.items():
                    if s_counter.get(letter, 0) < count:
                        valid = False
                        break

            j += 1

        return res