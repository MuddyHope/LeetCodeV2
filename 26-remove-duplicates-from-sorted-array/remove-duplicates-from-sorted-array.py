class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        seen_list = set()
        for each_num in nums[::-1]:
            if each_num in seen_list:
                nums.remove(each_num)
            else:
                seen_list.add(each_num)
