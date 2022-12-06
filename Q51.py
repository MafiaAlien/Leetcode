from typing import List 
class Solution:
    def __init__(self):
        self.res: List[List[str]] = []

    def solveNQueens(self, n: int) -> List[List[str]]:
        if not n:
            return []
        
        chessBoard = [["."] * n for _ in range(n)] # 构建棋盘
        self.backTracking(chessBoard, 0, n)
        return self.res 
    
    def backTracking(self,chessBoard: List[List[str]], row: int , n: int):
        # 如果递归层数为棋盘深度，那么存储结果并返回None
        if n == row:
            temp_res = []
            for temp in chessBoard:
                temp_str = "".join(temp)
                temp_res.append(temp_str)
            self.res.append(temp_res)

        for col in range(n):
            if not self.isValid(chessBoard, row, col):
                continue 
            chessBoard[row][col] = "Q"
            self.backTracking(chessBoard, row + 1, n)
            chessBoard[row][col] = "."

    def isValid(self, chessBoard: List[List[str]], row: int, col: int):
        for i in range(len(chessBoard)):
            # 列方向
            if chessBoard[i][col] == "Q":
                return False 

        i = row - 1
        j = col - 1 
        while i >= 0 and j >= 0:
            # 左对角线方向
            if chessBoard[i][j] == "Q":
                return False 

            i -= 1
            j -= 1 
        
        i = row - 1 
        j = col + 1
        while i >= 0 and j < len(chessBoard):
            # 右对角线方向
            if chessBoard[i][j] == "Q":
                return False 
            
            i -= 1
            j += 1 
        
        return True
if __name__ == "__main__":
    s = Solution()
    print(s.solveNQueens(6))
    
    #[['.Q....', '...Q..', '.....Q', 'Q.....', '..Q...', '....Q.'], ['..Q...', '.....Q', '.Q....', '....Q.', 'Q.....', '...Q..'], 
    #['...Q..', 'Q.....', '....Q.', '.Q....', '.....Q', '..Q...'], ['....Q.', '..Q...', 'Q.....', '.....Q', '...Q..', '.Q....']]
