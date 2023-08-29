# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        if not (head and head.next):
            return False 
        
        # 快慢指针, 环形链表终有一个点快慢指针可以交汇
        fast, slow = head.next, head
        while fast != slow:
            if not (fast and fast.next):
                # 链表到达了终点
                return False 
            else:
                fast = fast.next.next 
                slow = slow.next        
        return True # 交汇后返回True

        



