package main

func getIntersectionNode(headA, headB *ListNode) *ListNode {
	if headA == nil || headB == nil {
		return headA
	}

	curA := headA
	curB := headB

	for curA != curB {
		if curA == nil {
			curA = headB
		} else {
			curA = curA.Next
		}

		if curB == nil {
			curB = headA
		} else {
			curB = curB.Next
		}
	}
	return curA
}
