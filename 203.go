package main
func minSubArrayLen(target int, nums []int) int {
    slow := 0
    sum := 0
    res := len(nums) + 1
    for fast:=0; fast < len(nums); fast++ {
            sum += nums[fast]
            for sum >= target {
                subLength := fast - slow + 1
                if res > subLength {
                    res = subLength
                }
                sum -= nums[slow]
                slow ++
            }
    }
    if res == len(nums)+1 {
        return 0
    } else {
        return res
    }
}