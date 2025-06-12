class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        len_s = len(s)
        len_p = len(p)

        if len_s < len_p:
            return []
        
        p_count = {}
        for i in p:
            p_count[i] = 1 + p_count.get(i, 0)
        window_count = {}
        for j in s[:len_p]:
            window_count[j] = 1 + window_count.get(j, 0)

        res = []
        if p_count == window_count:
            res.append(0)

        for each in range(len_p, len_s):
            first_letter = s[each - len_p]
            last_letter = s[each]

            # Decrement the count of the letter going out of the window
            window_count[first_letter] -= 1
            if window_count[first_letter] == 0:
                del window_count[first_letter]

            # Increment the count of the new letter in the window
            window_count[last_letter] = 1 + window_count.get(last_letter, 0)

            if p_count == window_count:
                res.append(each - len_p + 1)

        return res
