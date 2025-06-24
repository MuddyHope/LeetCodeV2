class Solution:
    def isHappy(self, n: int) -> bool:
        seen = set()
        def backtrack(_sum , _len):
            if _sum in seen:
                return False
            seen.add(_sum)

            if int(_sum) > 1:
                curr_sum = 0
                for each in str(_sum):
                    curr_sum += int(each) ** 2
                return backtrack(curr_sum, len(str(curr_sum)))
            if int(_sum) == 1:
                return True

        return backtrack(n, len(str(n)))
        
           
            
