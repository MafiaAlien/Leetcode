from typing import Dict 
class Solution:
    def fourSumCount(self, nums1: List[int], nums2: List[int], nums3: List[int], nums4: List[int]) -> int:
        """
        首先iter前两个数组，求两数之和，并且把和当作key，出现的次数当作value存入一个hashmap
        接下来declare一个cnt变量存储总和为0的次数然后双循环iter剩下两个数组，如果0减去这两数组的数字之和刚好是hashmap中key的负数（0-（c+d））则cnt加上key后面的value（代表头两个数组中有n次得到这个和， 最后输出cnt
        """
        unordered_map:Dict = {}
        for m in nums1:
            for n in nums2:
                sum_ = m + n
                unordered_map[sum_] = unordered_map.get(sum_, 0) + 1

        cnt:int = 0

        for m in nums3:
            for n in nums4:
                k = -m-n 
                if k in unordered_map:
                    cnt += unordered_map[k]

        return cnt 