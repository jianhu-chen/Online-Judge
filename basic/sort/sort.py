#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import random
import unittest
from copy import deepcopy
from typing import List


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


def merge_sort(array: List[int]) -> List[int]:
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

    def _merge(left: List[int], right: List[int]) -> List[int]:
        i, j = 0, 0
        ret = []

        while i < len(left) and j < len(right):
            if left[i] <= right[j]:
                ret.append(left[i])
                i += 1
            else:
                ret.append(right[j])
                j += 1

        ret += left[i:]
        ret += right[j:]
        return ret

    def _divide(array: List[int]) -> List[List[int]]:
        if len(array) < 2:
            return array

        mid = len(array) // 2
        left = _divide(array[:mid])
        right = _divide(array[mid:])
        return _merge(left, right)

    return _divide(array)


def quick_sort(array):
    """
    快速排序.
    """
    n = len(array)
    if n < 2:
        return

    def _sort(array, start: int, end: int):
        if start >= end:
            return

        pivot = array[start]
        left, right = start, end
        while left < right:
            while left < right and array[right] > pivot:
                right -= 1
            array[left] = array[right]

            while left < right and array[left] <= pivot:
                left += 1
            array[right] = array[left]

        array[left] = pivot
        _sort(array, start, left - 1)
        _sort(array, left + 1, end)

    _sort(array, 0, len(array) - 1)


def heap_sort(array) -> List[int]:
    n = len(array)
    if n < 2:
        return

    def _heapify(array, idx: int, n: int = None):
        c1_idx = 2 * idx + 1
        c2_idx = 2 * idx + 2

        max_idx = idx
        if n is None:
            n = len(array)
        if c1_idx < n and array[c1_idx] > array[max_idx]:
            max_idx = c1_idx
        if c2_idx < n and array[c2_idx] > array[max_idx]:
            max_idx = c2_idx

        if max_idx != idx:
            array[idx], array[max_idx] = array[max_idx], array[idx]
            _heapify(array, max_idx, n)

    def _build_heap(array):
        n = len(array)
        latest_node_idx = n - 1
        parent_node_idx = (latest_node_idx - 1) // 2

        for i in range(parent_node_idx, -1, -1):
            _heapify(array, i)

    _build_heap(array)
    n = len(array)
    for i in range(n - 1, -1, -1):
        array[i], array[0] = array[0], array[i]
        _heapify(array, idx=0, n=i)


def shell_sort(array):
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
    assert min_value < max_value

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
            result = merge_sort(array)
            self.assertEqual(result, sorted(array))

    def test_quick_sort(self):
        for _ in range(TEST_TIMES):
            array = random_array()
            result = deepcopy(array)
            quick_sort(result)
            self.assertEqual(result, sorted(array))

    def test_heap_sort(self):
        for _ in range(TEST_TIMES):
            array = random_array()
            result = deepcopy(array)
            heap_sort(result)
            self.assertEqual(result, sorted(array))


if __name__ == "__main__":
    unittest.main()
