#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import time
import random
import unittest
from typing import List


class SplitSumClosed:
    """
    给定一个正数数组arr，
    请把arr中所有的数分成两个集合，尽量让两个集合的累加和接近
    返回最接近的情况下，较小集合的累加和
    """

    def solution1(self, arr: List[int]):
        pass

    def solution2(self, arr: List[int]):
        pass


class Tester(unittest.TestCase):

    def test_solution(self):
        obj = SplitSumClosed()
        s1_cost, s2_cost = 0, 0
        for _ in range(100):
            arr = [random.randint(1, 100) for _ in range(100)]
            s = time.perf_counter()
            ans1 = obj.solution1(arr)
            s1_cost += time.perf_counter() - s
            s = time.perf_counter()
            ans2 = obj.solution2(arr)
            s2_cost += time.perf_counter() - s
            self.assertEqual(ans1, ans2)
        print(f'solution1 cost: {s1_cost}')
        print(f'solution2 cost: {s2_cost}')


if __name__ == "__main__":
    arr = [1, 3, 5, 6]
    obj = SplitSumClosed()
    print(obj.solution1(arr))
    # unittest.main()
