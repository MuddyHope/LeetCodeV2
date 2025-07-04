class Solution:
    def maximumCount(self, nums: List[int]) -> int:
        # find minimum of the numlist

        # count_p = count_n = 0
        # for i in nums:
        #     if i == 0:
        #         continue
        #     if i > 0:
        #         count_p += 1
        #     else:
        #         count_n += 1
        # return max(count_p, count_n)
        def binary_search(nums: list[int], target):
            l, r = 0, len(nums)-1
            result = len(nums)

            while l <= r:
                mid = (l+r) //2
                if nums[mid] < target:
                    l = mid + 1
                else:
                    result = mid
                    r = mid -1
            return result


        # Binary-Search method
        neg_count = binary_search(nums, 0)
        first_positive = len(nums) - binary_search(nums, 1)
        return max(neg_count, first_positive)

