class Solution:
    def reverseBits(self, n: int) -> int:
        
        _bin = bin(n)[2:].zfill(32)
        print(_bin)

        return int(_bin[::-1], 2)