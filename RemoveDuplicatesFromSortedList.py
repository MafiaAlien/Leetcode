# Definition for singly-linked list.
from typing import List 
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return head 

        # set up a dummy head 

        dummy = ListNode(val=None, next=head)
        pre, cur = dummy, head 
        
        while cur:
            if pre.val == cur.val:
                # if pre's value is equal to cur.value 
                # connect pre's next to cur's next 
                pre.next = cur.next 
                cur = cur.next 
            else:
                # if value is different, move pointer
                pre, cur = cur, cur.next 
            
        return head

        