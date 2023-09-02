# Definition for singly-linked list.
from typing import Optional 
from listnode import ListNode

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        """
        判断两链表是否相交，即是判断它们的总长度是否相等：
        listA的非公共部分为a长度 listB的非公共部分为b长度  两链公共部分长度为c
        即用双指针分别指向A链和B链 其中一个链指针结束后指向另一个链的头部继续遍历 如果两链相交且两指针步长都为1步 则两指针的总路径长度相等 如果两指针同时为空 则两链不相交
        返回None
        """
        if not (headA and headB):
            return 
        
        curA = headA
        curB = headB

        while curA or curB:
            if curA is None:
                curA = headB

            if curB is None:
                curB = headA

            if curA == curB:
                return curA

            curA = curA.next
            curB = curB.next
        else: 
            return 