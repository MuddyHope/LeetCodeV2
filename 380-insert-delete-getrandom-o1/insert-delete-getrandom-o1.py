import random
class RandomizedSet:

    def __init__(self):
        self._set = {}
        

    def insert(self, val: int) -> bool:
        if val in self._set.keys():
            return False

        self._set[val] = None
        self._set[val] = 1
        return True

        

    def remove(self, val: int) -> bool:
        if val not in self._set.keys():
            return False
        del self._set[val]
        return True
        

    def getRandom(self) -> int:
        return random.choice(list(self._set.keys()))

        


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()