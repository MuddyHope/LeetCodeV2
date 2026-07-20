class Solution:
    def isValid(self, s: str) -> bool:
        

        hash_map = { "}": "{", "]": "[", ")": "("}

        stack = []

        for each in s:
            if stack and stack[-1] == hash_map.get(each):
                stack.pop()
            else:
                stack.append(each)
        
        return True if not stack else False