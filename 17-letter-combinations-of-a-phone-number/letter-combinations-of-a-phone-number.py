class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        hash_map = {
            2: "abc",
            3: "def",
            4: "ghi",
            5: "jkl",
            6: "mno",
            7: "pqrs",
            8: "tuv",
            9: "wxyz"
        }

        res = []

        def dfs(i, temp):
            print(f"i: {i}, temp: {temp}")

            if len(temp) == len(digits):
                res.append("".join(temp))
                return

            for letter in hash_map[int(digits[i])]:
                temp.append(letter)
                dfs(i + 1, temp)
                temp.pop()

        if not digits:
            return []

        dfs(0, [])
        return res