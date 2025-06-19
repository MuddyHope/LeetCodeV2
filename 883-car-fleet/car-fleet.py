class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        pair = [[pos,speed] for pos, speed in zip(position, speed)]
        stack = []
        for _p, _s in sorted(pair)[::-1]:
            stack.append((target - _p)/ _s)
            if len(stack) >= 2 and stack[-1] <= stack[-2]:
                stack.pop()
        return len(stack)