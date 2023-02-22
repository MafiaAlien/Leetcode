from typing import List

class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        if not intervals:
            return []
        intervals.sort(key= lambda x: x[0])
        res:List[List] = []
        # the first interval must exist with min left side after sorting
        res.append(intervals[0])
        for i in range(1, len(intervals)):
            last = res[-1]
            if last[1] >= intervals[i][0]:
                # left side did not change, right side in res compare with right num in 
                # current interval[i], the max one will be right num in res 
                res[-1] = [last[0], max(last[1], intervals[i][1])]
            else:
                res.append(intervals[i])
        return res
    
if __name__ == "__main__":
    intervals = [[1,3],[2,6],[8,10],[15,18]]
    s = Solution()
    print(s.merge(intervals=intervals))