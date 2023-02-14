from typing import List 
class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        five: int = 0
        ten: int = 0
        for bill in bills:
            if bill == 5:
                five += 1 
            elif bill == 10:
                five -= 1 
                ten += 1 
            else:
                # 20块分情况讨论， 有10块先找10块，没有10块才找5块
                if ten > 0 and five > 0:
                    ten -= 1 
                    five -= 1 
                elif five >  2:
                    five -= 3 
                else:
                    return False 
        else:
            return True 
                