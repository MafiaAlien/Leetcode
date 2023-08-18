from typing import Dict, List
class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        if not fruits:
            return 0
        freq: Dict = {}
        right: int = 0
        left: int = 0
        res: int = 0

        while right < len(fruits):
            freq[fruits[right]] = freq.get(fruits[right], 0) + 1
            
            if len(freq) > 2:
                freq[fruits[left]] -= 1
                if freq[fruits[left]] == 0:
                    freq.pop(fruits[left])
                left += 1

            res = max(res, right-left + 1)
            right += 1

        return res 
    
    if __name__ == "__main__":
        pass 