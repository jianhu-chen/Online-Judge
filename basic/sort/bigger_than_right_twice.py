#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import random
import unittest
from typing import List


class BiggerThanRightTwice:
    """
    在一个数组中, 对于任何一个数num, 求有多少个(后面的数*2)依然<num, 返回总个数
    比如: [3,1,7,0,2]
    3的后面有: 1, 0
    1的后面有: 0
    7的后面有: 0, 2
    0的后面没有
    2的后面没有
    所以总共有5个
    """

    def solution1(self, array: List) -> int:
        """
        暴力解法.
        """
        if not array:
            return 0

        ans = 0
        for idx in range(len(array)):
            for right in range(idx + 1, len(array)):
                if array[right] * 2 < array[idx]:
                    ans += 1
        return ans

    def solution2(self, array: List) -> int:
        """
        分治法.
        """

        def merge(array, L, M, R):
            i, j = L, M + 1
            help = []

            ans = 0
            while i <= M and j <= R:
                if array[i] < array[j]:
                    help.append(array[i])
                    i += 1
                else:
                    help.append(array[j])
                    k = L
                    # TODO (jianhu): 二分搜索第一个除2后依然大于等于array[j]的数
                    while k <= M:
                        if array[k] / 2 > array[j]:
                            break
                        k += 1
                    ans += M - k + 1
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


class TestBiggerThanRightTwice(unittest.TestCase):

    def test_bigger_than_right_twice(self):
        obj = BiggerThanRightTwice()
        for _ in range(TEST_TIMES):
            array = random_array()
            self.assertEqual(obj.solution1(array), obj.solution2(array))


if __name__ == "__main__":
    unittest.main()
