#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import random
import unittest


def swap(num1, num2):
    """不使用任何额外的变量, 交换两个数字的值."""
    num1 ^= num2
    num2 ^= num1
    num1 ^= num2
    return num1, num2


def one_number_odd_times(array):
    """https://leetcode.cn/problems/single-number.

    一个数组中只有一种数出现了奇数次, 其他数都出现了偶数次, 找到这个数并返回.
    """
    eor = 0
    for num in array:
        eor ^= num
    return eor


def two_number_odd_times(array):
    """https://leetcode.cn/problems/single-number-iii.

    一个数组中有两种数出现了奇数次, 其他数都出现了偶数次, 找到这两个数并返回(升序).
    """
    eor = 0
    for num in array:
        eor ^= num

    # 提取最右侧的1
    right_one = eor & (~eor + 1)
    num1 = 0
    for num in array:
        if right_one & num:
            num1 ^= num

    num2 = eor ^ num1
    return sorted([num1, num2])


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


class TestBitwise(unittest.TestCase):

    def test_swap(self):
        for _ in range(TEST_TIMES):
            num1, num2 = random.randint(0, 100), random.randint(0, 100)
            self.assertEqual(swap(num1, num2), (num2, num1))

    def test_one_number_odd_times(self):
        for _ in range(TEST_TIMES):
            array = random_array(min_size=2, remove_duplicate=True) * 2
            result = array.pop()
            random.shuffle(array)
            self.assertEqual(one_number_odd_times(array), result)

    def test_two_number_odd_times(self):
        for _ in range(TEST_TIMES):
            array = random_array(min_size=3, remove_duplicate=True)
            result = array[-2:]
            array *= 2
            array = array[:-2]
            random.shuffle(array)
            self.assertEqual(two_number_odd_times(array), sorted(result))


if __name__ == '__main__':
    unittest.main()
