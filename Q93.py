from typing import List

class Solution:
    def __init__(self):
        self.res: List[str] = []
    
    def restoreIpAddresses(self, s: str) -> List[str]:
        self._backtracking(s, 0, 0)
        return self.res 

    def _backtracking(self, s: str, startIndex: int, pointSum: int):
        if pointSum == 3 and self._isValid(s, startIndex, len(s)-1):
            # 终止条件，如果有三个分割点且地址合法则返回
            self.res.append(s[:])
            return 

        for i in range(startIndex, len(s)):
            if self._isValid(s, startIndex, i):
                s = s[:i+1] + '.' + s[i+1:]
                self._backtracking(s, i + 2, pointSum + 1) # 在填入.后，下一子串起始后移2位
                s = s[:i+1] + s[i+2:] # 回溯
            else:
                break

    @staticmethod
    def _isValid(s: str, start: int, end: int):
        """evaluate the valid ip"""
        if start > end:
            return False 

        if s[start] == "0" and start != end:
            # 开头是0不合法
            return False 
        
        if not 0 <= int(s[start:end+1]) <= 255:
            # 确保单一数字小于255
            return False
        return True