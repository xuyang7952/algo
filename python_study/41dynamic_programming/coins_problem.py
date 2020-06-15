"""
硬币找零问题，我们在贪心算法那一节中讲过一次。我们今天来看一个新的硬币找零问题。
假设我们有几种不同币值的硬币 v1，v2，……，vn（单位是元）。如果我们要支付 w 元，求最少需要多少个硬币。
比如，我们有 3 种不同的硬币，1 元、3 元、5 元，我们要支付 9 元，最少需要 3 个硬币（3 个 3 元的硬币）。
可以看做爬阶梯问题，分别可以走1.3.5步，怎么最少走到9步，动态转移方程为f(9)=1+min(f(8),f(6),f(4))
"""

from typing import List


def coins_dp(values: List, target: int):
    # memo[i]表示target为i的时候，所需的最少硬币数
    memo = [0] * (target + 1)
    memo[0] = 0

    for i in range(1, target + 1):
        min_num = 999999
        for n in values:
            if i >= n:
                min_num = min(min_num, 1 + memo[i - n])
            else:
                break
        memo[i] = min_num

    return memo[-1]


min_num = 999999


def coins_backtracking(values: List[int], target: int, cur_value: int, coins_count: int):
    if cur_value == target:
        global min_num
        min_num = min(min_num,coins_count)
    else:
        for n in values:
            if cur_value + n <= target:
                coins_backtracking(values, target, cur_value + n, coins_count + 1)


if __name__ == '__main__':
    values = [1, 3, 5]
    target = 23
    print(coins_dp(values, target))
    coins_backtracking(values, target, 0, 0)
    print(min_num)
