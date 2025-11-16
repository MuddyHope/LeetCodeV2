class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums_sorted = sorted(nums)
        n = len(nums_sorted)
        res = []
        seen = set()

        # value -> list of indices (to handle duplicates)
        hash_map = {}
        for i, v in enumerate(nums_sorted):
            hash_map.setdefault(v, []).append(i)

        for i in range(n):
            left, right = i + 1, n - 1

            while left < right:
                target = -(nums_sorted[i] + nums_sorted[left] + nums_sorted[right])

                # You only check the third value using your hashmap idea:
                # But since you're already using left+right, this becomes simpler:
                needed = -(nums_sorted[i] + nums_sorted[left])

                if nums_sorted[right] == needed:
                    triplet = (nums_sorted[i], nums_sorted[left], nums_sorted[right])

                    if triplet not in seen:
                        seen.add(triplet)
                        res.append(list(triplet))

                    left += 1
                    right -= 1
                
                elif nums_sorted[i] + nums_sorted[left] + nums_sorted[right] < 0:
                    left += 1
                else:
                    right -= 1

        return res
