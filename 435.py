from typing import List
class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        if not intervals:
            return 0 
        intervals.sort(key=lambda x: x[1]) # 按照有边界排序从小到大
        cnt: int = 1
        end = intervals[0][1]

        for i in range(1, len(intervals)):
            # 从左向右记录非交叉区间个数， 然后用总区间个数减去非交叉区间个数则等于需要去除的区间数    
            if end <= intervals[i][0]:
                cnt += 1
                end = intervals[i][1]
        return len(intervals) - cnt  

if __name__ == "__main__":
    pass 