class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        res = ""
        min_l = min(strs)
        for i in range(len(min_l)):       # checks flow
            for each in strs:               # checks strs
                if each[i] != min_l[i]:
                    return res
            res += each[i]
        return res