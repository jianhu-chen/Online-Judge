#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import time
import random
import string
import unittest


def get_index_of(str1: str, str2: str) -> int:
    """在str1中查找str2的位置, 如果找不到返回-1."""
    if len(str2) == 0 or len(str1) < len(str2):
        return -1

    for i in range(len(str1) - len(str2) + 1):
        if str1[i:i + len(str2)] == str2:
            return i

    return -1


def kmp(str1: str, str2: str) -> int:
    """在str1中查找str2的位置, 如果找不到返回-1."""
    if len(str2) == 0 or len(str1) < len(str2):
        return -1

    # next
    next = [-1 for _ in str2]
    if len(str2) > 1:
        next[1] = 0
        i = 2  # 目前在哪个位置上求next数组的值
        cn = 0  # 当前是哪个位置的值在和i-1位置的字符比较
        while i < len(str2):
            if str2[i - 1] == str2[cn]:
                next[i] = cn + 1
                i += 1
                cn += 1
            elif cn != -1:
                cn = next[cn]
            else:
                next[i] = 0
                i += 1

    i, j = 0, 0
    while i < len(str1) and j < len(str2):
        if str1[i] == str2[j]:
            i += 1
            j += 1
        elif next[j] != -1:
            j = next[j]
        else:
            i += 1

    return i - j if j == len(str2) else -1


def random_string(min_length: int, max_length: int) -> str:
    return "".join(
        random.choice(string.ascii_letters)
        for _ in range(random.randint(min_length, max_length))
    )


class Tester(unittest.TestCase):

    def test_kmp(self):
        TEST_TIMES = 100
        MIN_LENGTH = 1
        MAX_LENGTH = 100000
        cost_A, cost_B = 0, 0
        for _ in range(TEST_TIMES):
            str1 = random_string(MIN_LENGTH, MAX_LENGTH)
            str2 = random_string(MIN_LENGTH, MAX_LENGTH // 2)

            s = time.perf_counter()
            A = get_index_of(str1, str2)
            cost_A += time.perf_counter() - s

            s = time.perf_counter()
            B = kmp(str1, str2)
            cost_B += time.perf_counter() - s

            self.assertEqual(A, B)

        print("get_index_of cost: {} ms".format(cost_A * 1000 / TEST_TIMES))
        print("kmp cost: {} ms".format(cost_B * 1000 / TEST_TIMES))


if __name__ == "__main__":
    unittest.main()
