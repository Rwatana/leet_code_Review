# Time: O(n)
# Space: O(n)
import random


class RandomizedSet:

    def __init__(self):
        self.memo = {}
        self.pos = []
        
    def insert(self, val: int) -> bool:
        if val in self.memo:
            return False
        
        self.memo[val] = len(self.pos)
        self.pos.append(val)
        return True

    def remove(self, val: int) -> bool:
        if val not in self.memo:
            return False
        
        x = self.pos.pop()
        
        if x != val:
            self.memo[x] = self.memo[val]
            self.pos[self.memo[x]] = x
        
        del self.memo[val]
        return True
        
    def getRandom(self) -> int:
        return random.choice(self.pos)
