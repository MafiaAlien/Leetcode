# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        l1, l2 = list1, list2
        
        if not list1: 
            return l2 
        
        if not list2:
            return l1 
        # 创建一个dummyhead用于储存l1和l2节点对比后的新节点
        dummy = ListNode(val=-1, next=None)
        pre = dummy

        while l1 and l2:
            if l1.val <= l2.val:
                pre.next = l1
                l1 = l1.next # 指针移到下个节点，前节点deprecate
            else:
                pre.next = l2 
                l2 = l2.next 
            
            pre = pre.next # 将pre指针移动到下一个对比node和l1或者l2对比的node进行连接
        
        pre.next = l1 if l1 is not None else l2 # 更长一个链表的剩余节点直接放到后面（已sorted）
        return dummy.next # 返回新链表
        