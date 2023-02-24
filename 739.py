from typing import List
class Solution:
    def monotoneIncreasingDigits(self, n: int) -> int:
        str_num: List = list(str(n))
        for i in range(len(str_num)-1 , 0, -1):
            # 从尾部到头iter，如果前一位比后一位大，那么前一位剪1并且后面位数全部变9保证最大
            if int(str_num[i - 1]) > int(str_num[i]):
                # 前一位剪1
                str_num[i - 1] = str(int(str_num[i-1])-1)
                # 后面所有位置变成9
                str_num[i:] = '9' * (len(str_num) - i)
        return int("".join(str_num))