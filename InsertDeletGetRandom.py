
from random import choice
from typing import( 
    Dict, 
    List,
    )

class RandomizedSet:

    def __init__(self):
        self.nums: List[int] = []
        self.idx_mapping: Dict[int, int] = {}

    def insert(self, val: int) -> bool: 
        if val not in self.idx_mapping:
            # record index
            self.idx_mapping[val] = len(self.nums)
            # add value
            self.nums.append(val)
            return True
        return False 

    def remove(self, val: int) -> bool:
        if val in self.idx_mapping:
            # get last num and index of value needed to be removed
            swap_val, idx = self.nums[-1], self.idx_mapping[val]
            # replace number needed to beremoved with index of removed number to last number
            self.nums[idx] = swap_val
            # update dict kv pairs 
            self.idx_mapping[swap_val] = idx
            # delete number from mapping 
            del(self.idx_mapping[val])
            # delete swapped number from array
            self.nums.pop()
            return True
        return False 

    def getRandom(self) -> int:
        return choice(self.nums)
 
        





# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()