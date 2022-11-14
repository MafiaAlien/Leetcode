class Solution:
    def __init__(self):
        self.letter_map = {
            '2': 'abc',
            '3': 'def',
            '4': 'ghi',
            '5': 'jkl',
            '6': 'mno',
            '7': 'pqrs',
            '8': 'tuv',
            '9': 'wxyz'
        }
        self.string = "" # 临时字符串
        self.res = [] # 结果集
    
    def letterCombinations(self, digits: str) -> List[str]:
        self.res.clear()
        if not digits:
            return []
        i = 0 # 当前下标
        self.backtracking(digits, i)
        return self.res 

    def backtracking(self, digits, i):
        if i == len(digits): # 终止条件 如果下标等于目标长度
            self.res.append(self.string)
            return 

        digit = digits[i] # 取数字 
        letters = self.letter_map[digit] # 取数字对应的字母数组
        for letter in letters: # 遍历字母数组
            self.string += letter  # 添加入临时字符串进行组合
            self.backtracking(digits, i + 1) # 遍历下一层 i + 1
            self.string = self.string[:-1] # 回溯
        
