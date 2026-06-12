class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        

        # start from the right end, increment 1, if it becomes 0, then make sure you add that to the left most bit
        res = []
        

        # combine all of them together, add and then, return by splitting each digit
        _len = len(digits) - 1
        temp = 0
        i = 0
        while i < len(digits):
            temp += digits[i] * 10 ** _len
            _len -= 1
            i += 1

        temp += 1

        i = 0
        while i < len(str(temp)):
            res.append(int(str(temp)[i]))
            i += 1
        return res