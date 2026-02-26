from collections import Counter
class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        
        # s1 counter -> O(N)

        s1_counter = Counter(s1)

        s2_counter = {}
        # now we create a sliding window of len(s1) and iterate over s2

        left = 0
        for right in range(0, len(s2)):
            s2_counter[s2[right]] = 1 + s2_counter.get(s2[right], 0)
            # print(s2_counter, dict(s1_counter))
            if (right - left + 1) >= len(s1):
                if dict(s1_counter) == dict(s2_counter):
                    return True
                else:
                    s2_counter[s2[left]] -= 1
                    if s2_counter[s2[left]] == 0:
                        del s2_counter[s2[left]]
                    left += 1
        return False
            
            
