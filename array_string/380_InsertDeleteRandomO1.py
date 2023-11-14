import random 

# pop takes O(n)
class RandomizedSet1:

    def __init__(self):
        self.set = {}

    def insert(self, val: int) -> bool:
        if val not in self.set:
            self.set[val] = True
            return True
        else:
            return False

    def remove(self, val: int) -> bool:
        if val in self.set:
            self.set.pop(val)
            return True
        else:
            return False

    def getRandom(self) -> int:
        return random.choice(list(self.set.keys()))


# Optimal solution: O(1)
class RandomizedSet2:

    def __init__(self):
        self.numMap = {}
        self.numList = []
    
    def insert(self, val: int) -> bool:
        res = val not in self.numMap
        if res:
            self.numMap[val] = len(self.numList)
            self.numList.append(val)
        return res
    
    def remove(self, val: int) -> bool:
        res = val in self.numMap
        if res:
            # replace the remove val with the last val in numList
            idx = self.numMap[val]
            lastVal = self.numList[-1]
            self.numList[idx] = lastVal
            self.numList.pop()
            self.numMap[lastVal] = idx
            del self.numMap[val]
        return res

    def getRandom(self) -> int:
        return random.choice(self.numList)