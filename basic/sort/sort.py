#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import time
import random
import unittest
from copy import deepcopy
from typing import List


def timer(func):
    def wrapper(*args, **kwargs):
        start = time.perf_counter()
        func(*args, **kwargs)
        end = time.perf_counter()
        print("{:<30} cost: {} ms".format(func.__name__, (end - start) * 1000))
    return wrapper


def selection_sort(array: List[int]) -> None:
    """
    选择排序. 在无序区间中选择最小的元素, 将其放到有序区间的末尾.

    Parameters
    ----------
    array : List[int]
        待排序数组.
    """
    n = len(array)
    if n < 2:
        return

    for i in range(n - 1):
        min_num_idx = i
        for j in range(i + 1, n):
            if array[j] < array[min_num_idx]:
                min_num_idx = j

        if i != min_num_idx:
            array[i], array[min_num_idx] = array[min_num_idx], array[i]


def bubble_sort(array: List[int]) -> None:
    """
    冒泡排序. 在无序区间中通过连续比较相邻的元素, 将最大的元素放到有序区间的末尾.

    Parameters
    ----------
    array : List[int]
        待排序数组.
    """
    n = len(array)
    if n < 2:
        return

    for i in range(n - 1):
        for j in range(n - 1 - i):
            if array[j] > array[j + 1]:
                array[j], array[j + 1] = array[j + 1], array[j]


def insertion_sort(array: List[int]) -> None:
    """
    插入排序. 将无序区间中的每一个元素插入到有序区间中的适当位置.

    Parameters
    ----------
    array : List[int]
        待排序数组.
    """
    n = len(array)
    if n < 2:
        return

    for i in range(1, n):
        for j in range(i, 0, -1):
            if array[j] < array[j - 1]:
                array[j], array[j - 1] = array[j - 1], array[j]


def merge_sort(array: List[int]) -> None:
    """
    归并排序. 将无序区间分成两个子区间, 对每个子区间进行排序, 然后将两个排序好的子区间合并成一个有序区间.

    Parameters
    ----------
    array : List[int]
        待排序数组.

    Returns
    -------
    List[int]
        排序后的数组.
    """
    n = len(array)
    if n < 2:
        return

    def merge(array, L, M, R):
        i, j = L, M + 1
        help = []

        while i <= M and j <= R:
            if array[i] <= array[j]:
                help.append(array[i])
                i += 1
            else:
                help.append(array[j])
                j += 1

        while i <= M:
            help.append(array[i])
            i += 1

        while j <= R:
            help.append(array[j])
            j += 1

        array[L:R + 1] = help

    def process(array: List[int], L: int, R: int) -> None:
        if L == R:
            return

        M = L + ((R - L) >> 1)
        process(array, L, M)  # 处理左侧
        process(array, M + 1, R)  # 处理右侧
        merge(array, L, M, R)  # 合并两侧

    process(array, 0, len(array) - 1)


def _quick_sort_v1(array, L: int, R: int):
    if L >= R:
        return

    pivot = array[R]
    left = L - 1
    idx = L
    while idx < R:
        if array[idx] < pivot:
            left += 1
            array[left], array[idx] = array[idx], array[left]
        idx += 1
    left += 1
    array[left], array[R] = array[R], array[left]
    _quick_sort_v1(array, L, left - 1)
    _quick_sort_v1(array, left + 1, R)


def _quick_sort_v2(array, L: int, R: int):
    if L >= R:
        return

    pivot = array[R]
    left = L - 1
    right = R
    idx = L
    while idx < right:
        if array[idx] > pivot:
            right -= 1
            array[right], array[idx] = array[idx], array[right]
        elif array[idx] < pivot:
            left += 1
            array[left], array[idx] = array[idx], array[left]
            idx += 1
        else:
            idx += 1
    array[right], array[R] = array[R], array[right]
    _quick_sort_v2(array, L, left)
    _quick_sort_v2(array, right + 1, R)


def _quick_sort_v3(array, L: int, R: int):
    if L >= R:
        return

    # random pivot
    pivot_idx = random.randint(L, R)
    array[pivot_idx], array[R] = array[R], array[pivot_idx]
    _quick_sort_v2(array, L, R)


def quick_sort(array, version=3) -> None:
    """
    快速排序.
    """
    n = len(array)
    if n < 2:
        return

    {
        1: _quick_sort_v1,
        2: _quick_sort_v2,
        3: _quick_sort_v3,
    }[version](array, 0, n - 1)


def heap_sort(array):
    """
    堆排序.
    """
    n = len(array)
    if n < 2:
        return

    from heap import Heap
    h = Heap(max_size=n)
    h.build_heap(array)
    while not h.empty():
        array[n - 1] = h.pop()
        n -= 1


def count_sort(array):
    """
    计数排序.
    """
    n = len(array)
    if n < 2:
        return

    bucket = [0 for _ in range(max(array) + 1)]
    for num in array:
        bucket[num] += 1

    idx = 0
    for i in range(len(bucket)):
        while bucket[i] > 0:
            array[idx] = i
            idx += 1
            bucket[i] -= 1


def radix_sort(array):
    """
    基数排序.
    """
    n = len(array)
    if n < 2:
        return

    radix = 10  # 基数, 仅支持10进制

    # 找到最大数的位数
    max_num = max(array)
    max_digit = 0
    while max_num > 0:
        max_num //= radix
        max_digit += 1

    # 分配桶
    help = [0 for _ in range(n)]
    for d in range(max_digit):
        count = [0 for _ in range(radix)]
        for num in array:
            count[num // (radix ** d) % radix] += 1
        for i in range(1, radix):
            count[i] += count[i - 1]
        for i in range(n - 1, -1, -1):
            j = array[i] // (radix ** d) % radix
            help[count[j] - 1] = array[i]
            count[j] -= 1
        array[:] = help[:]


def shell_sort(array):
    """
    希尔排序. 插入排序的改进版本.
    希尔排序是把记录按下标的一定增量分组, 对每组使用直接插入排序算法排序
    随着增量逐渐减少, 每组包含的关键词越来越多, 当增量减至1时, 整个文件恰被分成一组, 算法便终止。
    """
    n = len(array)
    if n < 2:
        return

    gap = n
    while True:
        gap //= 2
        if gap == 0:
            return
        for i in range(gap, n):
            for j in range(i, 0, -gap):
                if array[j] < array[j - gap]:
                    array[j], array[j - gap] = array[j - gap], array[j]


TEST_TIMES = 1000
MIN_SIZE = 1
MAX_SIZE = 100
MIN_VALUE = 0
MAX_VALUE = 99999


def random_array(
    min_size: int = MIN_SIZE,
    max_size: int = MAX_SIZE,
    min_value: int = MIN_VALUE,
    max_value: int = MAX_VALUE,
    remove_duplicate: bool = False
) -> list:
    """
    Parameters
    ----------
    min_size : int
        The minimum size of the array.
    max_size : int
        The maximum size of the array.
    min_value : int
        The minimum value of the array.
    max_value : int
        The maximum value of the array.
    remove_duplicate : bool
        Whether to remove duplicate elements.

    Returns
    -------
    list
        A list of random integers.
    """
    assert min_size > 0 and max_size > 1 and min_value < max_value

    def _generate():
        size = random.randint(min_size, max_size)
        # range: [min_value, max_value]
        array = [random.randint(min_value, max_value) for _ in range(size)]
        if remove_duplicate:
            array = list(set(array))
        random.shuffle(array)
        return array

    array = _generate()
    while len(array) < min_size:
        array = _generate()
    return array


class TestSort(unittest.TestCase):

    def test_selection_sort(self):
        for _ in range(TEST_TIMES):
            array = random_array()
            result = deepcopy(array)
            selection_sort(result)
            self.assertEqual(result, sorted(array))

    def test_bubble_sort(self):
        for _ in range(TEST_TIMES):
            array = random_array()
            result = deepcopy(array)
            bubble_sort(result)
            self.assertEqual(result, sorted(array))

    def test_insertion_sort(self):
        for _ in range(TEST_TIMES):
            array = random_array()
            result = deepcopy(array)
            insertion_sort(result)
            self.assertEqual(result, sorted(array))

    def test_merge_sort(self):
        for _ in range(TEST_TIMES):
            array = random_array()
            result = deepcopy(array)
            merge_sort(result)
            self.assertEqual(result, sorted(array))

    def test_quick_sort(self):
        for _ in range(TEST_TIMES):
            array = random_array()
            result1 = deepcopy(array)
            result2 = deepcopy(array)
            result3 = deepcopy(array)
            sorted_array = sorted(array)
            quick_sort(result1, version=1)
            quick_sort(result2, version=2)
            quick_sort(result3, version=3)
            self.assertEqual(result1, sorted_array)
            self.assertEqual(result2, sorted_array)
            self.assertEqual(result3, sorted_array)

    def test_heap_sort(self):
        for _ in range(TEST_TIMES):
            array = random_array()
            result = deepcopy(array)
            heap_sort(result)
            self.assertEqual(result, sorted(array))

    def test_count_sort(self):
        for _ in range(TEST_TIMES):
            array = random_array()
            result = deepcopy(array)
            count_sort(result)
            self.assertEqual(result, sorted(array))

    def test_radix_sort(self):
        for _ in range(TEST_TIMES):
            array = random_array()
            result = deepcopy(array)
            radix_sort(result)
            self.assertEqual(result, sorted(array))

    def test_shell_sort(self):
        for _ in range(TEST_TIMES):
            array = random_array()
            result = deepcopy(array)
            shell_sort(result)
            self.assertEqual(result, sorted(array))


if __name__ == "__main__":
    unittest.main()
