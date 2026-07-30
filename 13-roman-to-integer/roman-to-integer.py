class Solution:
    def romanToInt(self, s: str) -> int:
        hash_map = {
            "I":            1,
            "V":            5,
            "X":           10,
            "L":          50,
            "C":            100,
            "D":           500,
            "M":       1000
        }

        res = 0
        stack = []

        for i in range(len(s)):
            if stack and hash_map[stack[-1]] < hash_map[s[i]]:
                res += hash_map[s[i]] - hash_map[stack[-1]] - hash_map[stack[-1]]
            else:
                stack.append(s[i])
                res += hash_map[s[i]]
        return res

        