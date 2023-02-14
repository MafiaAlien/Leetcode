from typing import List 

class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        start:int = 0
        curSum:int = 0
        totalSum:int = 0 
        for i in range(len(gas)):
            curSum += gas[i] - cost[i]  
            totalSum += gas[i] - cost[i]
            if curSum < 0:
                # 如果当前和为0，则下个节点当作起点
                curSum = 0
                start = i + 1
        
        if totalSum < 0:
            # 穷尽所有的起点，没有能回来的
            return -1 
        return start            


if __name__ == "__main__":
    pass 