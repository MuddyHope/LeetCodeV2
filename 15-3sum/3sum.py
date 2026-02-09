class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
    
        seen = set()

        res = []

        for i in range(len(nums) - 2):
            left, right = i + 1, len(nums) - 1

            while left < right:
                # print(f"combination : {i} {left} {right}")

                curr_sum = nums[i] + nums[left] + nums[right]
                if curr_sum == 0:
                    # print(f"added combination: {i} {left} {right}")
                    if tuple(sorted((nums[i], nums[left], nums[right]))) not in seen:
                        seen.add(tuple(sorted((nums[i], nums[left], nums[right]))))
                        res.append([nums[i], nums[left], nums[right]])
                    left += 1
                    right -= 1

                elif curr_sum > 0:
                    right -= 1
                else:
                    left += 1
        # print("seen", seen)
        return res

            
