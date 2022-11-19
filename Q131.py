from typing import List 
class Solution:
    def __init__(self):
        self.path: List= []
        self.res: List[List]= []

    
    def partition(self, s: str) -> List[List[str]]:
        self.backtracking(s, 0)
        return self.res 

    def backtracking(self, s: str, startIndex: int):
        if startIndex >= len(s): # 终止条件
            self.res.append(self.path[:])
            return 

        for i in range(startIndex, len(s)):  
            temp = s[startIndex:i+1] # 临时字符，startIndex就是切割线
          
            if temp == temp[::-1]: # 判断是否回文，如果是则添加入路径
                self.path.append(temp) # 满足回文加入路径
                self.backtracking(s, i + 1)
                self.path.pop() # 回溯
            else:
                continue

if __name__ =="__main__":
    string = "aabddaeggeeda"
    s = Solution()
    print(s.partition(string))