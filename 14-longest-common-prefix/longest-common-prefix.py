class Solution:
    def longestCommonPrefix(self, v: List[str]) -> str:
        ans=""
        v=sorted(v)
        print(v)
        first=v[0]
        last=v[-1]
        for i in range(min(len(first),len(last))):
            print(i)
            if(first[i]!=last[i]):
                return ans
            ans+=first[i]
        return ans 