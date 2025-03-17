class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        
        # def merge():
        #     ...

        # def break_it(start, high, nums):
        #     while start != high:
        #         break_it(start, mid, nums)
        #         break_it(mid+1, high, nums)
        #     merge(start, mid, nums)
        #     merge()

        # start, mid, high = 0, len(nums) //2, len(nums) - 1
        # break_it(start, mid, high, nums)
        return sorted(nums)
