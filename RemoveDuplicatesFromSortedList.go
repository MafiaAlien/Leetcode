package main
 // Definition for singly-linked list.

 type ListNode struct {
	Val int
	Next *ListNode
}

func deleteDuplicates(head *ListNode) *ListNode {
	   if head == nil {
		 return nil
	   }

	   dummy := &ListNode {
		 Val: -1,
		 Next: head,
	   }
	   pre := dummy 
	   cur := head 

	   for cur != nil {
			 if pre.Val != cur.Val {
			   pre = cur
			   cur = cur.Next
			 } else {
			   pre.Next = cur.Next
			   cur = cur.Next
			 }
	   }

	   return head
}