class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        
        number_dict = {2: "abc", 3:"def", 4:"ghi", 5:"jkl", 6:"mno", 7:"pqrs", 8:"tuv", 9:"wxyz"}
        res = []
        if not digits:
            return res

        subset = ""
        def dfs(i):
            nonlocal subset
            # print(f"i: {i}, subset: {subset}")
            if len(subset) == len(digits):
                res.append(subset)
                return
            if i > len(digits):
                return

            for each in number_dict[int(digits[i])]:
                subset += each
                # print(f"before dfs: {subset}")
                dfs(i+1)
                # print(f"after dfs: {subset}")
                subset = subset[:len(subset)-1]
        
        dfs(0)

        return res