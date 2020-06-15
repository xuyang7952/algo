"""
简单正则实现
"""

is_match = False


def rmatch(r_idx: int, m_idx: int, regex: str, main: str):
    """
    简单的正则匹配，
    :param r_idx: 模式串的下标,
    :param m_idx: 主串的下标
    :param regex: 模式串
    :param main: 主串
    :return:
    """
    global is_match
    if is_match: return

    if r_idx >= len(regex):
        # 匹配成功
        is_match = True
        return

    if m_idx >= len(main) and r_idx < len(regex):
        # 模式串没匹配完，主串已经结束了，匹配失败
        is_match = False
        return

    if regex[r_idx] == "*":
        # * 匹配1个或多个任意字符，递归搜索每一种情况
        for i in range(m_idx, len(main)):
            rmatch(r_idx + 1, i + 1, regex, main)
    elif regex[r_idx] == "?":
        # ? 匹配0个或1个任意字符，两种情况
        rmatch(r_idx + 1, m_idx, regex, main)
        rmatch(r_idx + 1, m_idx + 1, regex, main)
    else:
        if regex[r_idx] == main[m_idx]:
            rmatch(r_idx + 1, m_idx + 1, regex, main)


if __name__ == '__main__':
    regex = 'ab*eee?d'
    # main = 'abcdsadfkjlekjoiwjiojieeecd'
    main = 'bcdsadfkjlekjoiwjiojieeecd'
    rmatch(0, 0, regex, main)
    print(is_match)
