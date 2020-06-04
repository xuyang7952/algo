""" 冒泡排序，插入排序，选择排序"""

from typing import List


def bubble_sort(array: List[int]):
    n = len(array)
    for i in range(n):
        flag = False
        for j in range(n - i - 1):
            if array[j] > array[j + 1]:
                array[j], array[j + 1] = array[j + 1], array[j]
            flag = True
        if not flag:
            break


def insert_sort(array: List[int]):
    n = len(array)
    for i in range(1, n, 1):
        value = array[i]
        j = i - 1
        # 这里不使用range，是因为range中的index不符合需求，先判断
        while j >= 0 and a[j] > value:
            a[j + 1] = a[j]
            j -= 1
        array[j + 1] = value


def select_sort(array: List[int]):
    n = len(array)
    for i in range(n):
        min_index = i
        for j in range(i, n):
            if array[j] < array[min_index]:
                min_index = j
        array[i], array[min_index] = array[min_index], array[i]


if __name__ == '__main__':
    a = [3, 4, 2, 1, 5, 6, 7, 8]
    # bubble_sort(a)
    # insert_sort(a)
    select_sort(a)
    print(a)
