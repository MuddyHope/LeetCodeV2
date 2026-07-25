class Solution:
    def hammingWeight(self, n: int) -> int:
        _bin = str(bin(n)[2:])

        i = 0
        res = 0
        print(type(_bin))
        while i < len(_bin):
            if _bin[i] == "1":
                res += 1
            i += 1
        return res