class Solution:
    def lexicalOrder(self, n: int) -> List[int]:
        res = []

        subset = 1
        def dfs(i):
            print(i)
            if i > n:
                return
            res.append(i)

            for x in range(10):
                dfs(i*10+x)
        for x in range(1,10):
            dfs(x)
        
        return res
    


