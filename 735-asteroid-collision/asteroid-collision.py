class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:

        stack = []

        for each in asteroids:

            while stack and each < 0 and stack[-1] > 0:

                if abs(stack[-1]) < abs(each):
                    # stack asteroid explodes
                    stack.pop()

                elif abs(stack[-1]) > abs(each):
                    # current asteroid explodes
                    each = 0
                    break

                else:
                    # both explode
                    stack.pop()
                    each = 0
                    break

            if each != 0:
                stack.append(each)

        return stack