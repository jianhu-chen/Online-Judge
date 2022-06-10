#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import random
import unittest
from copy import deepcopy

from basic.sort import (
    heap_sort,
    merge_sort,
    quick_sort,
    bubble_sort,
    insertion_sort,
    selection_sort
)
from basic.bitwise import swap, one_number_odd_times, two_number_odd_times
from basic.examples import (
    local_minimum,
    binary_search_exist,
    binary_search_near_left,
    binary_search_near_right
)

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


if __name__ == "__main__":
    unittest.main()
