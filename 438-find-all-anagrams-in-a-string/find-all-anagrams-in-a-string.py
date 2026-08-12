class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        res = []

        p_counter = dict(Counter(p))

        l = 0
        c_dict = {}
        for r in range(len(s)):
            c_dict[s[r]] = 1 + c_dict.get(s[r], 0)
            # print(f"l,r: {l, r}, c_dict: {c_dict}")

            if c_dict == p_counter:
                res.append(l)
                
            while r-l+1 >= len(p):
                c_dict[s[l]] = c_dict[s[l]] - 1
                if c_dict[s[l]] == 0:
                    del c_dict[s[l]]
                l += 1
        return res
