class Solution:
    def evalRPN(self, tokens: List[str]) -> int:

        stack = deque()

        for each in tokens:
            # print(f"current op: {each}, type: {type(each)}")

            # check number
            try:
                num = int(each)
                stack.append(num)
                # print(stack)
                continue
            except:
                pass

            if each == "+":
                a = stack.pop()
                b = stack.pop()
                stack.append(b + a)
            elif each == "-":
                a = stack.pop()
                b = stack.pop()
                stack.append(b - a)
            elif each == "*":
                a = stack.pop()
                b = stack.pop()
                stack.append(b * a)
            elif each == "/":
                a = stack.pop()
                b = stack.pop()
                stack.append(int(b / a))   # truncate toward zero

            # print(stack)

        return stack[-1]
