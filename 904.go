package main

func totalFruit(fruits []int) int {
	if len(fruits) == 0 {
		return 0
	}
	left := 0
	freq := map[int]int{}
	res := 0
	for right, i := range fruits {
		freq[i]++
		if len(freq) > 2 {
			freq[fruits[left]]--
			if freq[fruits[left]] == 0 {
				delete(freq, fruits[left])
			}
			left++
		}
		res = max(res, right-left+1)
	}
	return res
}

func max(a, b int) int {
	if b > a {
		return b
	} else {
		return a
	}
}
