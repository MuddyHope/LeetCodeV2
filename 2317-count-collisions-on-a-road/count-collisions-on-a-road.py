class Solution:
    def countCollisions(self, directions: str) -> int:
        trimmed = directions.lstrip('L').rstrip('R')

        # All 'L' and 'R' in this trimmed section will eventually collide with something
        return sum(1 for c in trimmed if c in ('L', 'R'))

