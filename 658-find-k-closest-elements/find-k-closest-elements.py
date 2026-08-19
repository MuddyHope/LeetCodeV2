class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        res = []
        nums = arr
        l, r = 0, len(arr) -1
        i = 0
        while l <= r:
            if abs(nums[l]-x) <= abs(nums[r]-x) and nums[l] < nums[r]:
                heapq.heappush(res, ( (abs(nums[l] - x)), nums[l] ))
                l += 1
            else:
                heapq.heappush(res, ((abs(nums[r] - x)), nums[r]))
                r -= 1
            i += 1
    
        out = []
        j = 0
        print(len(list(res)))
        while j < k:
            _abs, numb = heapq.heappop(res)
            out.append(numb)
            j += 1
        return sorted(out[:k])
            