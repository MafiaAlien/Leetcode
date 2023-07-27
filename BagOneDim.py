from typing import List 
def test_1_dim_bag_problem(bag_size: int, weight: List[int], value: List[int]) -> List[int]:
    dp: List[int] = [0] * (bag_size + 1)
    num_items = len(weight)
    for i in range(num_items): # 遍历物品
        # 倒序iter背包，防止01背包中每个物品重复添加（相比于正序遍历）
        for j in range(bag_size, weight[i] - 1, -1):
            dp[j] = max(dp[j], dp[j - weight[i]] + value[i])

    return dp

def main(): 
    weight = [1, 3, 4]
    value = [15, 20, 30]
    bag_weight = 4
    print(test_1_dim_bag_problem(bag_weight, weight, value))

if __name__ == '__main__':
    main()