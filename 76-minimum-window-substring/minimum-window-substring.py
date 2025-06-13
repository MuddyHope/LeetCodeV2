from collections import Counter
class Solution:
    def minWindow(self, s: str, t: str) -> str:
        # t is the slider per se.
        # s is the the final

        # first approach
        '''
        Have a set that has all the available substring, loop over the set and take the least number of 
        '''
        '''
        Now for it loop over s with size t, break out of the loop once you have a match
        '''
        res = ""
        t_count = Counter(t)
        window_count = {}

        left = 0
        min_len = float('inf')
        min_window = ""

        for right in range(len(s)):
            # Add current character to window
            window_count[s[right]] = window_count.get(s[right], 0) + 1

            # While window contains all chars in t, try shrinking it
            while all(window_count.get(ch, 0) >= count for ch, count in t_count.items()):
                current_window_len = right - left + 1
                if current_window_len < min_len:
                    min_len = current_window_len
                    min_window = s[left:right+1]

                # Remove the left char and shrink window
                window_count[s[left]] -= 1
                if window_count[s[left]] == 0:
                    del window_count[s[left]]
                left += 1
        return min_window




        


        