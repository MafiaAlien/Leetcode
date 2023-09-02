package main

func fourSumCount(nums1 []int, nums2 []int, nums3 []int, nums4 []int) int {
	hashmap := make(map[int]int)
	for _, a := range nums1 {
		for _, b := range nums2 {
			hashmap[a+b]++
		}
	}
	cnt := 0

	for _, c := range nums3 {
		for _, d := range nums4 {
			cnt += hashmap[-c-d]
		}
	}

	return cnt
}
