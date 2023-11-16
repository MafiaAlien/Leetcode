from typing import Dict
class Solution:
    def isStrobogrammatic(self, num: str) -> bool:
        mapping: Dict = {
            '0': '0',
            '1': '1',
            '6': '9',
            '8': '8',
            '9': '6',
        }

        l:int = 0
        
        while l <= len(num) // 2: # 考虑个位数的情况
            if num[l] not in mapping:
                return False 
            if mapping[num[l]] != num[len(num) - 1 -l]:
                return False 
            l += 1
        else:
            return True 
