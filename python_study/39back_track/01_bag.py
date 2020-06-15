"""
01 背包问题
"""
from typing import List

# 背包中的物品列表
picks = []
picks_with_max_value = []


def get_value(items_info: List, picks: List):
    # 返回背包总
    values = [item[1] for item in items_info]
    return sum(a * b for a, b in zip(values, picks))


def bag(capacity: int, cur_weight: int, items_info: List, pick_idx: int):
    """
    回溯法解01背包，穷举
    :param capacity: 背包容量
    :param cur_weight: 背包当前重量
    :param items_info: 物品的重量和价值信息
    :param pick_idx: 当前物品的索引
    :return:
    """
    # 背包装满了，或者未装满但循环完所有的物品
    if pick_idx >= len(items_info) or cur_weight == capacity:
        global picks_with_max_value
        if get_value(items_info, picks) > get_value(items_info, picks_with_max_value):
            picks_with_max_value = picks.copy()
    else:
        item_weight = items_info[pick_idx][0]
        # 类似于二叉树，对于一个物品，只有选取放入和不选不放入这两个选择；不断分叉，每个分叉仍然调用该函数，直到终止条件：
        # 背包已经装满了，或者是未装满，但已经遍历了所有的物品；
        # 选取，放入背包
        if cur_weight + item_weight <= capacity:
            picks[pick_idx] = 1
            bag(capacity, cur_weight + item_weight, items_info, pick_idx + 1)
        # 不选，不放入
        picks[pick_idx] = 0
        bag(capacity, cur_weight, items_info, pick_idx + 1)


if __name__ == '__main__':
    # [(weight, value), ...]
    items_info = [(1, 2), (2, 2), (1, 4), (3, 5), (4, 10)]
    capacity = 8

    print('--- items info ---')
    print(items_info)

    print('\n--- capacity ---')
    print(capacity)

    picks = [0] * len(items_info)
    bag(capacity, 0, items_info, 0)

    print('\n--- picks ---')
    print(picks_with_max_value)

    print('\n--- value ---')
    print(get_value(items_info, picks_with_max_value))