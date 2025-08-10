class Solution:
    def addDigits(self, num: int) -> int:
        num_str = str(num)
        curr_sum = num

        while len(num_str) != 1:
            curr_sum = 0
            for each in num_str:
                curr_sum += int(each)
            num_str = str(curr_sum)
            # print(curr_sum)
        return curr_sum