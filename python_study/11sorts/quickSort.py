"""快速排序，首先是应用了分治递归的思想；实现的思想，取一个阈值，将数组分为两个数组，小于阈值的，阈值，大于阈值的；
实现的方法：两个指针，i，j，i就是要找的分位点，a[0:i]i之前的数据是小于阈值的，j遍历整个数组，一旦小于阈值，和a[i]做交换，i++"""

from typing import List


def partiton(arr: list, p: int, r: int):
    pivot = arr[r]
    i = p
    j = p
    # i之前的数据都是小于阈值的，j用来遍历整个列表，插入排序,i就是要找的分位点
    while j <= (r - p):
        if arr[j] < pivot:
            arr[i], arr[j] = arr[j], arr[i]
            i += 1
        j += 1
    arr[i], arr[r] = arr[r], arr[i]
    return i


def qucikSort(arr: List, p: int, r: int):
    if p >= r:
        return
    q = partiton(arr, p, r)

    qucikSort(arr, p, q - 1)
    qucikSort(arr, q + 1, r)


def quick_sort(ls, idx_start, idx_end):
    if idx_end - idx_start <= 0:
        return

    pivot = idx_end
    i = idx_start
    for j in range(i, idx_end + 1):
        if ls[j] <= ls[pivot]:
            ls[i], ls[j] = ls[j], ls[i]
            if j == pivot:
                pivot = i
            i += 1
    quick_sort(ls, idx_start, pivot - 1)
    quick_sort(ls, pivot + 1, idx_end)


if __name__ == '__main__':
    a = [3, 4, 2, 1, 5, 6, 8, 7]
    # bubble_sort(a)
    # insert_sort(a)
    n = len(a)
    qucikSort(a, 0, n - 1)
    # quick_sort(a, 0, n - 1)
    print(a)
