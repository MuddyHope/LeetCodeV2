from collections import Counter
class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:

        if len(s1) > len(s2):
            return False


        s1_counter = Counter(s1)
        print(s1_counter)


        s1_len = len(s1)
        i= 0
        j = i + len(s1)


        while j <= len(s2):
            if Counter(s2[i:j]) == s1_counter:
                return True
            i += 1
            j = i + len(s1)


        return False
        

