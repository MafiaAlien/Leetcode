package main

func hasCycle(head *ListNode) bool {
	if head == nil || head.Next == nil {
		return false
	}
	fast := head.Next
	slow := head

	for fast != slow {
		if fast == nil || fast.Next == nil {
			return false
		} else {
			fast = fast.Next.Next
			slow = slow.Next
		}
	}
	return true

}
