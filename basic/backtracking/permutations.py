#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import random
import unittest
from typing import List
from itertools import permutations


class Permutations:
    """
    给定一个不含重复数字的数组 nums ，返回其 所有可能的全排列 。你可以 按任意顺序 返回答案。

    https://leetcode.cn/problems/permutations/
    """

    def solution(self, nums: List[int]) -> List[List[int]]:
        def process(record: List[int], rest: List[int]):
            if rest == []:
                return [record]
            ans = []
            for idx in range(len(rest)):
                ans += process([*record, rest[idx]], rest=rest[:idx] + rest[idx + 1:])
            return ans
        return process([], nums)


class Tester(unittest.TestCase):

    def test_solution(self):
        obj = Permutations()
        for _ in range(10):
            nums = [random.randint(-10000, 10000) for _ in range(random.randint(0, 10))]
            nums = list(set(nums))  # 去重
            ans = obj.solution(nums)
            for ans_i, gt_i in zip(ans, permutations(nums)):
                self.assertEqual(ans_i, list(gt_i))


if __name__ == "__main__":
    unittest.main()
