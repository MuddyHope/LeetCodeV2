class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        s_stack, t_stack = [], []

        for each in s:
            if each != "#":
                s_stack.append(each)
            elif s_stack:
                s_stack.pop()
        

        for each in t:
            if each != "#":
                t_stack.append(each)
            elif t_stack:
                t_stack.pop()
        return s_stack == t_stack
        