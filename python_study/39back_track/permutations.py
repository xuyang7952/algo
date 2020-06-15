"""
全排列
"""

from typing import List

# 全排列的记录列表
permutations_list = []


def permutations(nums: List, n: int, pick_count: int):
    """
    从nums选取n个数的全排列
    :param nums:
    :param pick_count:
    :return:
    """
    if n == 0:
        print(permutations_list)
    else:
        # 遍历数组
        for i in range(len(nums)):
            permutations_list[pick_count] = nums[i]
            # 更新剩余的数组
            nums_new = nums.copy()
            del nums_new[i]
            permutations(nums_new, n - 1, pick_count + 1)


if __name__ == '__main__':
    nums = [1, 2, 3, 4]
    n = 3
    permutations_list = [0] * n
    permutations(nums, n, 0)
