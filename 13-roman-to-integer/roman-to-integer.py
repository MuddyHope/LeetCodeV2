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


        # IV
        res = 0
        i = 0
        stack = []
        while i < len(s):
            print(f"stack: {stack}, letter: {s[i]}")
            if stack and hash_map.get(stack[-1]) < hash_map[s[i]]:      # check I < V
                res -= hash_map[stack[-1]]
                res += hash_map.get(s[i]) - hash_map[stack.pop()]
            else:
                stack.append(s[i])
                res += hash_map.get(s[i])
            i += 1
        return res



