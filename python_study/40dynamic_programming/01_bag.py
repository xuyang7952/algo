from typing import List, Tuple


def bag(items_info: List[int], capacity: int):
    """
    固定容量的背包，计算能装进背包的物品组合的最大重量
    :param items_info: 每个物品的重量
    :param capacity:背包容量
    :return:最大的装载重量
    """
    n = len(items_info)
    # 构建一个二维数据（n* capacity+1） 代表这个循环到该物品这一层，能够达到的状态--即装了多少重量的物品
    memo = [[0] * (capacity + 1) for i in range(n)]
    memo[0][0] = 1
    if items_info[0] <= capacity:
        memo[0][items_info[0]] = 1

    # 针对每个物品进行遍历，代表二维数组中的行，每一层
    for i in range(1, n):
        # 针对背包容量的每个状态进行遍历，下标代表背包的装载量，例如index=6时，值为0代表未达到这个装载量，1代表背包装载重量为6.
        for cur_weight in range(capacity + 1):
            # 上一层达到的容量的状态是下一层的基础，
            if memo[i - 1][cur_weight] != 0:
                memo[i][cur_weight] = memo[i - 1][cur_weight]  # 不选的情况，就和上一层相同列的值相同
                if cur_weight + items_info[i] <= capacity:  # 选，并不超过总重量
                    memo[i][cur_weight + items_info[i]] = 1
    print("memo:", memo)
    for w in range(capacity, -1, -1):
        # 二维数组中的最后一行数据，index对应的value值是1，最大的index就是背包可以装载最大的重量
        if memo[-1][w] != 0:
            return w


def bag_with_max_value(items_info: List[Tuple[int, int]], capacity: int):
    """
    固定容量的背包，计算能装进背包的物品组合的最大价值
    :param items_info:物品的重量和价值
    :param capacity:背包容量
    :return:最大装载价值
    """
    n = len(items_info)
    memo = [[-1] * (capacity + 1) for _ in range(n)]
    memo[0][0] = 0
    if items_info[0][0] <= capacity:
        memo[0][items_info[0][0]] = items_info[0][1]

    # 针对每个物品进行遍历，代表二维数组中的行，每一层
    for i in range(1, n):
        # 针对背包容量的每个状态进行遍历，下标代表背包的装载量，例如index=6时，值为-1代表未达到这个装载量，
        # 其他值，代表达到这个装载量时的物品的总价值
        for cur_weight in range(capacity + 1):
            # 上一层达到的容量的状态是下一层的基础;每一层都是截至为止，背包中可以装载的重量。
            if memo[i - 1][cur_weight] != -1:
                memo[i][cur_weight] = memo[i - 1][cur_weight]
                if cur_weight + items_info[i][0] <= capacity:
                    # memo[i][cur_weight + items_info[i][0]],可能存在相同的重量的装载方法，取最大价值的装法。
                    memo[i][cur_weight + items_info[i][0]] = max(memo[i][cur_weight + items_info[i][0]],
                                                                 memo[i - 1][cur_weight] + items_info[i][1])
    print("memo max value:", memo)
    # 取最后一行的最大值
    return max(memo[-1])


if __name__ == '__main__':
    # [weight, ...]
    items_info = [2, 2, 4, 6, 1]
    capacity = 9
    print(bag(items_info, capacity))
    # [(weight, value), ...]
    items_info = [(3, 5), (4, 2), (4, 4), (4, 2), (4, 10)]
    capacity = 9
    print(bag_with_max_value(items_info, capacity))
