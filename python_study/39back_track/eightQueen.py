"""
八皇后的问题
"""

# 定义棋盘尺寸
BOARD_SIZE = 4
solution_count = 0
queen_list = [0] * BOARD_SIZE


def is_valid_pos(cul_column: int, pos: int):
    i = 0
    while i < cul_column:
        # 同行，（同列）
        if queen_list[i] == pos:
            return False
        # 同对角线
        if cul_column - i == abs(pos - queen_list[i]):
            return False
        i += 1
    return True


def eight_queens(cul_column: int):
    """
    循环嵌套八层，每层循环都递归调用，并判断是否满足条件，不满足，就会回退到上一层的循环的函数调用，改变上一层的棋子放置的位置；
    这个就是回溯算法。所有的循环结束后，即得到所有的结果。
    输出所有符合要求的八皇后序列
    用一个长度为8的数组代表棋盘的列，数组的数字则为当前列上皇后所在的行数;
    可以将棋盘数设置为4；循环递归比较容易能看懂；
    :param cul_column:
    :return:
    """
    if cul_column >= BOARD_SIZE:
        # 循环到最后一层，仍然满足，queen_list存储的就是一个解
        global solution_count
        solution_count += 1
        print(queen_list)
    else:
        for i in range(BOARD_SIZE):
            # 如果可以放置，记录放置pos，并且进入下一层循环;
            # 如果不可以放置（本层，不可以放置或者是下一层的放置失败，返回False），则移动本层的棋子位置
            if is_valid_pos(cul_column, i):
                queen_list[cul_column] = i
                eight_queens(cul_column + 1)


if __name__ == '__main__':
    eight_queens(0)
    print(solution_count)
