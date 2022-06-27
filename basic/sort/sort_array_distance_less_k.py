#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import heapq
import unittest
from typing import List


class SortArrayDistanceLessK:
    """
    已知一个几乎有序的数组。几乎有序是指, 如果把数组排好顺序的话, 每个元素移动的距离一定不超过k
    k相对于数组长度来说是比较小的。请选择一个合适的排序策略, 对这个数组进行排序。
    """

    def solution(self, array: List, k: int) -> None:
        heap = []
        idx = 0
        while idx < len(array) and idx < k:
            heapq.heappush(heap, array[idx])
            idx += 1

        sorted_idx = 0
        while len(heap) != 0:
            array[sorted_idx] = heapq.heappop(heap)
            sorted_idx += 1
            if idx < len(array):
                heapq.heappush(heap, array[idx])
                idx += 1


class Tester(unittest.TestCase):

    def test_solution(self):
        array = [3, 1, 2, 5, 4, 6, 9, 7, 8, 10]
        k = 3
        SortArrayDistanceLessK().solution(array, k)
        self.assertEqual(array, [1, 2, 3, 4, 5, 6, 7, 8, 9, 10])


if __name__ == "__main__":
    unittest.main()
