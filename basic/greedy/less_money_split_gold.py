#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import heapq
import random
import unittest
from typing import List
from itertools import permutations


class LessMoneySplitGold:
    """
    一块金条切成两半, 是需要花费和长度数值一样的铜板的. 比如长度为20的金条, 不管怎么切, 都要花费20个铜板.

    一群人想整分整块金条, 怎么分最省铜板？输入一个数组, 返回分割的最小代价.

    例如：

    给定数组{10,20,30}, 代表一共三个人,  整块金条长度为10 + 20 + 30 = 60, 金条要分成10, 20, 30三个部分 (不考虑顺序).

    如果先把长度60的金条分成10和50, 花费60: 再把长度50的金条分成20和30, 花费50;一共花费110铜板.

    但如果先把长度60的金条分成30和30, 花费60: 再把长度30金条分成10和20, 花费30: 一共花费90铜板.
    """

    def solution1(self, arr: List[int]):
        def process(arr):
            """返回划分arr的最小代价."""
            if len(arr) == 1:
                return 0
            candidates = permutations(arr)
            ans = float('inf')
            for candidate in candidates:
                candidate = list(candidate)
                a = candidate.pop(0)
                b = candidate.pop(0)
                candidate.append(a + b)
                ans_i = process(candidate) + (a + b)
                if ans_i < ans:
                    ans = ans_i
            return ans
        return process(arr)

    def solution2(self, arr: List[int]):
        heap = arr[:]
        heapq.heapify(heap)
        ans = 0
        while len(heap) > 1:
            a = heapq.heappop(heap)
            b = heapq.heappop(heap)
            ans += (a + b)
            heapq.heappush(heap, a + b)
        return ans


class Tester(unittest.TestCase):

    def test_solution(self):
        import time
        obj = LessMoneySplitGold()
        s1_cost = 0
        s2_cost = 0
        for _ in range(1000):
            length = random.randint(1, 5)
            arrs = [random.randint(1, 100) for _ in range(length)]
            s1 = time.perf_counter()
            ans1 = obj.solution1(arrs)
            s1_cost += time.perf_counter() - s1
            s2 = time.perf_counter()
            ans2 = obj.solution2(arrs)
            s2_cost += time.perf_counter() - s2
            self.assertEqual(ans1, ans2)
        print("solution1 cost:", s1_cost)
        print("solution2 cost:", s2_cost)


if __name__ == "__main__":
    unittest.main()
