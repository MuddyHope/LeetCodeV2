class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        # lets go with 2 pointers approach
        left, right = 0 , len(numbers) - 1
        while left <= right:
            curr_sum = numbers[left] + numbers[right]
            if target == curr_sum:
                return [left+1, right+1]
            if curr_sum > target:
                right -= 1
            else:
                left += 1
    
        