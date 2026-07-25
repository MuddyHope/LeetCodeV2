class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        
        def helper(s) -> list:
            i = 0
            stack = []
            while i < len(s):
                print(f"curr: {s[i]}, stack: {stack}")
                if stack and s[i] == "#":
                    stack.pop()
                else:
                    stack.append(s[i])
                    if s[i] == "#":
                        stack.pop()
                i += 1
            return stack

        
        
        return helper(s) == helper(t)
