class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        my_number_dict = {"2": "abc", "3": "def", "4": "ghi", "5": "jkl", "6": "mno",
        "7": "pqrs", "8": "tuv", "9": "wxyz"}

        res = []
        if not digits:
            return res
        
        stack = [("", 0)]

        while stack:
            curr, idx = stack.pop()
            if idx == len(digits):
                res.append(curr)
            else:
                for each_letter in my_number_dict[digits[idx]]:
                    stack.append((curr + each_letter, idx +1))
        return res


        
        

