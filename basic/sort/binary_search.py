#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import random
import unittest
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


class TestExamples(unittest.TestCase):

    def test_binary_search_exist(self):
        for _ in range(TEST_TIMES):
            array = random_array(remove_duplicate=True)
            array.sort()
            if random.random() > 0.5:
                num = random.choice(array)
            else:
                num = random.randint(0, MAX_VALUE)
            index = array.index(num) if num in array else -1
            self.assertEqual(binary_search_exist(array, num), index)

    def test_binary_search_near_left(self):
        for _ in range(TEST_TIMES):
            array = random_array()
            if random.random() > 0.5:
                num = random.choice(array)
            else:
                num = random.randint(0, 2 * MAX_VALUE)
            index = -1
            array.sort()
            for i in range(len(array)):
                if array[i] >= num:
                    index = i
                    break
            self.assertEqual(binary_search_near_left(array, num), index)

    def test_binary_search_near_right(self):
        for _ in range(TEST_TIMES):
            array = random_array()
            if random.random() > 0.5:
                num = random.choice(array)
            else:
                num = random.randint(-MAX_VALUE, MAX_VALUE)
            index = -1
            array.sort()
            for i in range(len(array) - 1, -1, -1):
                if array[i] <= num:
                    index = i
                    break
            self.assertEqual(binary_search_near_right(array, num), index)

    def test_local_minimum(self):
        for _ in range(TEST_TIMES):
            array = random_array(remove_duplicate=True)
            i = local_minimum(array)
            if i != -1:
                if i != 0:
                    self.assertTrue(array[i - 1] > array[i], (i, array))
                if i != len(array) - 1:
                    self.assertTrue(array[i] < array[i + 1], (i, array))
            else:
                for i in range(len(array)):
                    if i != 0:
                        self.assertFalse(array[i - 1] > array[i])
                    if i != len(array) - 1:
                        self.assertFalse(array[i] < array[i + 1])


if __name__ == '__main__':
    unittest.main()
