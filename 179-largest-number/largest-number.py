class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        
        # sorting based on the first character
        array = list(map(str, nums))
        
        array.sort(key= lambda x: x*10, reverse=True)
        
        # print(array)
        if array[0] == '0':
            return "0"

        res = "".join(array)
        return res
        