class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:

        def stacker(word):
            stack = []
            for each in word:
                if each != "#":
                    stack.append(each)
                    continue
                elif stack: 
                    stack.pop()
            return stack


        s_stack = stacker(s)
        t_stack = stacker(t)

        return s_stack == t_stack

        
        
                