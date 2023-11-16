from typing import List 
class TwoSum:

    def __init__(self):
        self.nums: List = []
        # make sure num array is sorted
        self.isSorted: bool = False 

    def add(self, number: int) -> None:
        self.nums.append(number)
        self.isSorted = False 

    def find(self, value: int) -> bool:
        """
        two pointer and sort the nums array
        """
        if not self.isSorted:
            self.nums.sort()
            self.isSorted = True

        low, high = 0, len(self.nums) - 1 # two pointer

        while low < high:
            curSum = self.nums[low] + self.nums[high]

            if curSum < value:
                low += 1 
            elif curSum > value:
                high -= 1 
            else: return True
        return False 


# Your TwoSum object will be instantiated and called as such:
# obj = TwoSum()
# obj.add(number)
# param_2 = obj.find(value)