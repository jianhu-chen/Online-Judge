#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import random
import unittest
from typing import List


class SmallSum:
    """
    在一个数组中，一个数左边比它小的数的总和，叫该数的小和
    所有数的小和累加起来，叫数组小和
    例子:  [1,3,4,2,5]
    1左边比1小的数: 没有
    3左边比3小的数: 1
    4左边比4小的数: 1、3
    2左边比2小的数: 1
    5左边比5小的数: 1、3、4、 2
    所以数组的小和为1+1+3+1+1+3+4+2=16
    给定一个数组arr, 求数组小和
    """

    def solution1(self, array: List) -> int:
        """
        暴力解法.
        """
        if not array:
            return 0

        ans = 0
        for idx in range(len(array)):
            left_sum = 0
            for left in range(idx):
                if array[left] < array[idx]:
                    left_sum += array[left]
            ans += left_sum
        return ans

    def solution2(self, array: List) -> int:
        """
        分治法.
        """
        if not array:
            return 0

        def merge(array, L, M, R):
            i, j = L, M + 1
            help = []
            ans = 0
            while i <= M and j <= R:
                if array[i] < array[j]:
                    help.append(array[i])
                    ans += (R - j + 1) * array[i]
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
            return ans

        def process(array, L, R):
            if L == R:
                return 0

            M = L + ((R - L) >> 1)
            return process(array, L, M) + process(array, M + 1, R) + merge(array, L, M, R)

        return process(array, 0, len(array) - 1)


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


class TestSmallSum(unittest.TestCase):

    def test_small_sum(self):
        ss = SmallSum()
        for _ in range(TEST_TIMES):
            array = random_array()
            self.assertEqual(ss.solution1(array), ss.solution2(array))


if __name__ == "__main__":
    unittest.main()
