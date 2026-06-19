class Solution:
    def minWindow(self, s: str, t: str) -> str:
        
        if len(s) < len(t):
            return ""

        res = ""
        resLen = float("inf")

        counter = dict(Counter(t))
        window = {}

        have, need = 0, len(counter)
        l = 0
        for r in range(len(s)):
            window[s[r]] = 1 + window.get(s[r], 0)

            if s[r] in counter and window[s[r]] == counter[s[r]]:
                have += 1
            
            while have == need:
                # update res
                if (r-l + 1) < resLen:
                    res = s[l:r+1]
                    resLen = r -l +1
                
                window[s[l]] -= 1
                if s[l] in counter and window[s[l]] < counter[s[l]]:
                    have -= 1
                l += 1
        return res if resLen != float("inf") else ""



