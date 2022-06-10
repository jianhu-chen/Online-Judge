# -*- coding: utf-8 -*-
from typing import List


def binary_search_exist(sorted_array: List, num: int) -> int:
    """
    查找数组中是否存在某个数字并返回下标.

    Returns
    -------
    int
        如果存在返回下标, 否则返回-1.
    """
    L, R = 0, len(sorted_array) - 1
    while L <= R:
        mid = L + ((R - L) >> 1)
        focus_num = sorted_array[mid]
        if num < focus_num:
            R = mid - 1
        elif num > focus_num:
            L = mid + 1
        else:
            return mid
    return -1


def binary_search_near_left(sorted_array: List, num: int) -> int:
    """
    查找大于等于某个数字的最小的数字的位置.

    Returns
    -------
    int
        如果存在返回下标, 否则返回-1.
    """
    index = -1  # 默认不存在
    L, R = 0, len(sorted_array) - 1
    while L <= R:
        mid = L + ((R - L) >> 1)
        focus_num = sorted_array[mid]
        if num > focus_num:
            L = mid + 1
        else:
            index = mid
            R = mid - 1
    return index


def binary_search_near_right(sorted_array: List, num: int) -> int:
    """
    查找小于等于某个数字的最大的数字的位置.

    Returns
    -------
    int
        如果存在返回下标, 否则返回-1.
    """
    index = -1  # 默认不存在
    L, R = 0, len(sorted_array) - 1
    while L <= R:
        mid = L + ((R - L) >> 1)
        focus_num = sorted_array[mid]
        if num < focus_num:
            R = mid - 1
        else:
            index = mid
            L = mid + 1
    return index


def local_minimum(array: List[int]):
    """
    找到非空无序数组中的任意一个局部最小值并返回下标.
    数组中任意相邻两数都不相等.

    Returns
    -------
    int
        下标.
    """
    if len(array) == 1:
        return 0

    if array[0] < array[1]:
        return 0

    if array[-1] < array[-2]:
        return len(array) - 1

    L, R = 0, len(array) - 1
    while L <= R:
        mid = L + ((R - L) >> 1)
        if mid > 0 and array[mid - 1] < array[mid]:
            R = mid - 1
        elif mid < len(array) - 1 and array[mid + 1] < array[mid]:
            L = mid + 1
        else:
            return mid
