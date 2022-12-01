from typing import *

class Solution:
    def __init__(self) -> None:
        self.fragment: List[int] = [] 

    def canConstruct(self, seq: List[int], subseq: List[List[int]]) -> bool:
        curSubPointer: int = 0
        while curSubPointer < len(subseq):
            self.fragment.clear()
            if self.backTracking(seq, subseq[curSubPointer], 0):
                curSubPointer += 1
            else:
                return False 
        else:
            return True 

    def backTracking(self, seq: List[int], subseq: List[int], startIndex: int) -> bool:
        if startIndex >= len(seq):
            return 
        
        for i in range(startIndex, len(seq)):
            self.fragment.append(seq[i])
            
            if self.fragment[:] == subseq[:]:
                return True 
            else:
                self.backTracking(seq, subseq, i + 1)
                self.fragment.pop()
        
        return False 
    
            

def main():
    s = Solution()
    print(s.canConstruct([1, 2, 3, 4, 5], [[1,2], [3,4], [5]])) # True
    print(s.canConstruct([1, 3, 4, 5, 2], [[2, 3], [1, 3], [4, 2], [2], [4, 5]])) # True
    print(s.canConstruct([1, 2, 3, 4, 5], [[2, 3], [3], [1, 2], [4, 5]])) # True 
    print(s.canConstruct([1, 2, 3, 4, 5], [[2,3],[1,3], [4,2], [4,5]] )) # False 


if __name__ == "__main__":
    main()
   
    