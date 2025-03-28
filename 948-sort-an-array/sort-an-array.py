class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        if len(nums) > 1:
            mid = len(nums)//2
            L = nums[:mid]
            R = nums[mid:]

            self.sortArray(L)
            self.sortArray(R)
            # print(f"L is {L}")
            # print(f"R is {R}")
            i = j = k = 0
            while i < len(L) and j < len(R):
                # print(f"i: {i}, j: {j}, k: {k}")

                if L[i] < R[j]:
                    nums[k] = L[i]
                    i += 1
                else:
                    nums[k] = R[j]
                    j += 1
                k += 1
            
            while i < len(L):
                nums[k] = L[i]
                i += 1
                k += 1
            
            while j < len(R):
                nums[k] = R[j]
                j += 1
                k += 1
        return nums
                