#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Copyright (c) Sina Weibo, Inc. and its affiliates.
import random
import unittest
from typing import List


class NetherlandsFlag:
    """
    荷兰国旗问题: 给定一个数组和一个数字num, 将数组中所有小于num的元素移到数组的前面, 大于等于num的元素移到数组的后面.
    """

    def solution(self, array: List[int], num: int) -> None:
        if len(array) < 1:
            return

        left = -1
        idx = 0
        while idx < len(array):
            if array[idx] < num:
                left += 1
                array[left], array[idx] = array[idx], array[left]
            idx += 1


class NetherlandsFlagV2:
    """
    荷兰国旗问题2: 给定一个数组和一个数字num, 将数组中所有小于num的元素移到数组的前面, 等于num的元素移到数组中间, 大于num的元素移到数组后面.
    """

    def solution(self, array: List[int], num: int) -> None:
        if len(array) < 1:
            return

        left = -1
        right = len(array)
        idx = 0
        while idx < right:
            if array[idx] > num:
                right -= 1
                array[right], array[idx] = array[idx], array[right]
            elif array[idx] < num:
                left += 1
                array[left], array[idx] = array[idx], array[left]
                idx += 1
            else:
                idx += 1


TEST_TIMES = 10000
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


class Tester(unittest.TestCase):

    def test_netherlands_flag(self):
        obj = NetherlandsFlag()
        for _ in range(TEST_TIMES):
            array = random_array()
            num = random.randint(MIN_VALUE, MAX_VALUE)
            obj.solution(array, num)
            check_flag = False
            for i in range(len(array)):
                if array[i] >= num:
                    check_flag = True
                if check_flag:
                    self.assertGreaterEqual(array[i], num, (array, num))

    def test_netherlands_flag_v2(self):
        obj = NetherlandsFlagV2()
        for _ in range(TEST_TIMES):
            array = random_array()
            num = random.randint(MIN_VALUE, MAX_VALUE)
            obj.solution(array, num)
            check_equal_flag = False
            check_grater_flag = False
            for i in range(len(array)):
                if array[i] == num:
                    check_equal_flag = True
                if array[i] > num:
                    check_grater_flag = True
                if check_equal_flag:
                    self.assertGreaterEqual(array[i], num)
                if check_grater_flag:
                    self.assertGreater(array[i], num)


if __name__ == "__main__":
    unittest.main()
