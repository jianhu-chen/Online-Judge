#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import time
import random
import string
import unittest


def timer(func):
    def wrapper(*args, **kwargs):
        start = time.perf_counter()
        func(*args, **kwargs)
        end = time.perf_counter()
        print("{:<30} cost: {} ms".format(func.__name__, (end - start) * 1000))
    return wrapper


def palindrome_str(str: str) -> int:
    str = "#" + "#".join(list(str)) + "#"
    max_length = 0
    for i in range(len(str)):
        offset = 0
        while i - offset >= 0 and i + offset < len(str):
            if str[i - offset] != str[i + offset]:
                break
            max_length = max(max_length, 1 + 2 * offset)
            offset += 1

    return max_length // 2


def manacher_str(str: str) -> int:
    str = "#" + "#".join(list(str)) + "#"
    max_r = 0
    # 回文半径数组
    array = [1 for _ in str]
    C = -1  # 中心
    R = -1  # 最大回文半径
    for i in range(len(str)):
        # 至少不用验证的回文半径
        array[i] = min(array[2 * C - i], R - i) if i < R else 1

        offset = array[i]
        while i - offset >= 0 and i + offset < len(str):
            if str[i - offset] != str[i + offset]:
                break
            offset += 1
        array[i] = offset

        if i + array[i] > R:
            C, R = i, i + array[i]
        max_r = max(max_r, array[i])

    return max_r - 1


def random_string(min_length: int, max_length: int) -> str:
    return "".join(
        random.choice(string.ascii_letters)
        for _ in range(random.randint(min_length, max_length))
    )


class TestPalindrome(unittest.TestCase):

    def test_manacher_str(self):
        TEST_TIMES = 10  # 10w times test
        MIN_LENGTH = 1
        MAX_LENGTH = 100000
        for _ in range(TEST_TIMES):
            s = random_string(MIN_LENGTH, MAX_LENGTH)
            self.assertEqual(palindrome_str(s), manacher_str(s))


if __name__ == "__main__":
    unittest.main()
