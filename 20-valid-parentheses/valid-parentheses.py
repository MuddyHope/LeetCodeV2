class Solution:
    def isValid(self, s: str) -> bool:
        my_stack = []
        my_dict = {"}": "{", ")": "(", "]": "["}
        
        # append to stack each loop
        for each in s:
            if my_stack and my_dict.get(each) == my_stack[-1]:
                my_stack.pop()
            else:
                my_stack.append(each)
        if my_stack:
            return False
        return True


        
