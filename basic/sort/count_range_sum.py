#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import random
import unittest
from typing import List


class CountRangeSum:
    """给定一个数组arr, 两个整数lower和upper, 返回arr中有多少个子数组的累加和在[lower,upper]范围上.

    示例1:
    输入: nums = [-2,5,-1], lower = -2, upper = 2
    输出: 3
    解释: 存在三个区间: [0,0], [2,2] 和 [0,2], 对应的区间和分别是: -2 、-1 、2

    示例 2:
    输入: nums = [0], lower = 0, upper = 0
    输出: 1

    ref: https://leetcode.cn/problems/count-of-range-sum
    """

    def solution1(self, array: List, lower: int, upper: int) -> int:
        """暴力解法."""
        if not array:
            return 0

        ans = 0
        for i in range(len(array)):
            for j in range(i, len(array)):
                subsum = sum(array[i:j + 1])
                if lower <= subsum <= upper:
                    ans += 1
        return ans

    def solution2(self, array: List, lower: int, upper: int) -> int:
        """分治法."""
        if not array:
            return 0

        def merge(pre_sum, L, M, R, lower, upper):
            ans = 0
            i, left, right = L, M + 1, M + 1
            while i <= M:
                while left <= R and pre_sum[left] - pre_sum[i] < lower:
                    left += 1
                while right <= R and pre_sum[right] - pre_sum[i] <= upper:
                    right += 1
                ans += (right - left)
                i += 1

            i, j = L, M + 1
            help = []
            while i <= M and j <= R:
                if pre_sum[i] <= pre_sum[j]:
                    help.append(pre_sum[i])
                    i += 1
                else:
                    help.append(pre_sum[j])
                    j += 1

            while i <= M:
                help.append(pre_sum[i])
                i += 1

            while j <= R:
                help.append(pre_sum[j])
                j += 1

            pre_sum[L:R + 1] = help

            return ans

        def process(pre_sum, L, R, lower, upper):
            if L == R:
                return 1 if lower <= pre_sum[L] <= upper else 0

            M = L + ((R - L) >> 1)
            return sum([
                process(pre_sum, L, M, lower, upper),
                process(pre_sum, M + 1, R, lower, upper),
                merge(pre_sum, L, M, R, lower, upper)
            ])

        pre_sum = []
        s = 0
        for num in array:
            s += num
            pre_sum.append(s)

        return process(pre_sum, 0, len(pre_sum) - 1, lower, upper)


TEST_TIMES = 10000
MIN_SIZE = 3
MAX_SIZE = 99
MIN_VALUE = -100
MAX_VALUE = 100


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


class TestCountRangeSum(unittest.TestCase):

    def test_small_sum(self):
        obj = CountRangeSum()
        for _ in range(TEST_TIMES):
            array = random_array()
            lower = random.randint(MIN_VALUE, MAX_VALUE // 2)
            upper = random.randint(MAX_VALUE // 2, MAX_VALUE)
            self.assertEqual(
                obj.solution1(array, lower, upper),
                obj.solution2(array, lower, upper),
                array
            )


if __name__ == "__main__":
    unittest.main()
