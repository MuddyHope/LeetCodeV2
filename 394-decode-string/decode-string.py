class Solution:
    def decodeString(self, s: str) -> str:
        
        alpha_stack = []
        num_stack = []
        curr = 0

        i = 0
        while i < len(s):
            print(f"curr: {s[i]}")
            if s[i].isdigit():
                curr = (curr * 10 ) + int(s[i])
            
            else:
                if s[i] == "[":
                # opening
                    num_stack.append(curr)
                    curr = 0
                    alpha_stack.append(s[i])
                elif s[i] == "]":
                    temp = ""

                    while alpha_stack and alpha_stack[-1] != "[":
                        temp = alpha_stack.pop() + temp
                    alpha_stack.pop()
                    num = num_stack.pop()

                    alpha_stack.append(temp * num)
                else:
                    alpha_stack.append(s[i])
    
            i += 1
        
        ans = ""
        while alpha_stack:
            ans = alpha_stack.pop() + ans
        
        return ans