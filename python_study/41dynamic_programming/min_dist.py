"""
二维数组的最短路径,
什么是动态规划，动态规划就是，为了解决穷举算法的的指数型增长的世界复杂度，
而采取的分阶段的穷举法，只是每个阶段，只会保留一个最优解，这样就大大降低了，算法的时间复杂度。
"""

from typing import List
from itertools import accumulate


def min_dist(weights: List[List[int]]):
    """
     二维数组中的，寻找最短路径，从右下角到左上角
    :param weights:
    :return:
    """
    m, n = len(weights), len(weights[0])
    table = [[0] * n for _ in range(m)]
    # table 是m*n的二维数组，table[i][j] 代表左上角的起始点到该位置的最小路径的值
    table[0] = list(accumulate(reversed(weights[-1])))
    for i, v in enumerate(accumulate(row[-1] for row in reversed(weights))):
        table[i][0] = v

    for i in range(1, m):
        for j in range(1, n):
            table[i][j] = weights[~i][~j] + min(table[i - 1][j], table[i][j - 1])
    print("table:", table)

    return table[-1][-1]


def min_dist2(weights: List[List[int]]):
    """
    二维数组中的，寻找最短路径，从左上角到右下角
    :param weights:
    :return:
    """
    m, n = len(weights), len(weights[0])
    table = [[0] * n for _ in range(m)]
    # 二维数组第一行求和
    table[0] = list(accumulate(weights[0]))
    # 二维数组，第一列求和
    for i, v in enumerate(accumulate(row[0] for row in weights)):
        table[i][0] = v
    for i in range(1, m):
        for j in range(1, n):
            # table[i][j] 只能从左边的，或者上边的过来，取两个可能中的小的值
            table[i][j] = weights[i][j] + min(table[i - 1][j], table[i][j - 1])
    print("table:", table)
    return table[-1][-1]


def min_dist_recur(weights: List[List[int]]):
    """
    递归方式实现，寻找最短路径
    :param weights:
    :return:
    """
    m, n = len(weights), len(weights[0])
    table = [[0] * n for _ in range(m)]

    def min_dist_to(i: int, j: int):
        if i == 0 and j == 0: return weights[0][0]
        if table[i][j] > 0: return table[i][j]
        # 查找左边，和上面的最小值
        min_left = float("inf") if j <= 0 else min_dist_to(i, j - 1)
        min_up = float("inf") if i <= 0 else min_dist_to(i - 1, j)
        return weights[i][j] + min(min_left, min_up)

    res = min_dist_to(m - 1, n - 1)
    print("table:", table)
    return res


if __name__ == '__main__':
    weights = [[1, 3, 5, 9], [2, 1, 3, 4], [5, 2, 6, 7], [6, 8, 4, 3]]
    print(min_dist(weights))
    print(min_dist2(weights))
    print(min_dist_recur(weights))
    print(float("inf"))
