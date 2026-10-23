class Solution:
    def maximumTastiness(self, price: list[int], k: int) -> int:
        
        # vals = combinations(price, k)
        # res = []
        # curr_max = 0
        # for each_combi in vals:
        #     temp = []
        #     # print(f"curr: {each_combi}")
        #     for each in combinations(each_combi, 2):
        #         temp.append(abs(each[0] - each[1]))
        #     # print(f"temp: {temp}")
        #     res.append(min(temp))
        # return max(res)

        price.sort()
        
        l = 0
        r = price[-1] - price[l]
        res = 0
        while l <= r:
            mid = (l+r)//2
            ret = self.helper_fn(price, mid, k)
            if ret != -1:
                res = max(res, ret)
                l = mid + 1
            else:
                r = mid - 1
        return res
        
    def helper_fn(self, price, mid, k) -> int:
        cnt = 1
        l = price[0]
        for i in range(1, len(price)):
            if price[i] >= mid + l:
                l = price[i]
                cnt += 1
        
        if cnt >= k:
            return mid
        else:
            return -1


