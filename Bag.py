from typing import List

def test_2_dim_bag_problem(bag_size: int, weight: List[int], value: List[int]) -> List[int]:
    rows, cols = len(weight), bag_size + 1
    dp = [[0 for _ in range(cols)] for _ in range(rows)]

    # dp initialize
    for i in range(rows):
        dp[i][0] = 0
    
    first_item_weight, first_item_value = weight[0], value[0]

    for j in range(1, cols):
        if first_item_weight <= j:
            dp[0][j] = first_item_value

    # updating dp array, iter item first then iter bag
    for i in range(1, len(weight)):
        cur_item_weight, cur_item_val = weight[i], value[i]
        for j in range(1, cols):
            if cur_item_weight > j: # Backpack does not fit current item
                dp[i][j] = dp[i-1][j] # skip current item 不放物品i
            else:
                # add item i
                dp[i][j] = max(dp[i-1][j], dp[i-1][j - cur_item_weight] + cur_item_val) # current item, comparing with previous item's value and select the larger one
    
    return dp


def main():
    bag_size = 4
    weight = [1, 3, 4]
    value = [15, 20, 30]
    print(test_2_dim_bag_problem(bag_size, weight, value))


if __name__ == '__main__':
    main()