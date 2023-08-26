package main

func removeDuplicates(nums []int) int {
	if nums == nil {
		return -1
	}

	slow := 0

	for fast := 1; fast < len(nums); fast++ {
		if nums[slow] != nums[fast] {
			if fast-slow > 0 {
				nums[slow+1] = nums[fast]
				slow++
			}
		}
	}
	res := slow + 1
	return res
}
