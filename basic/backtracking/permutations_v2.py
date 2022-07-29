#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import random
import unittest
from typing import List
from itertools import permutations


class Permutations:
    """
    给定一个可包含重复数字的序列 nums ，按任意顺序 返回所有不重复的全排列。

    https://leetcode.cn/problems/permutations-ii/
    """

    def solution(self, nums: List[int]) -> List[List[int]]:
        def process(record: List[int], rest: List[int]):
            if rest == []:
                return [record]
            ans = []
            visited = set()
            for idx in range(len(rest)):
                if rest[idx] not in visited:
                    ans += process([*record, rest[idx]], rest=rest[:idx] + rest[idx + 1:])
                    visited.add(rest[idx])
            return ans
        return process([], nums)


class Tester(unittest.TestCase):

    def test_solution(self):
        obj = Permutations()
        for _ in range(10):
            nums = [random.randint(-10, 10) for _ in range(random.randint(0, 10))]
            ans = obj.solution(nums)
            gt_set = set("_".join(map(str, x)) for x in permutations(nums))
            self.assertEqual(len(ans), len(gt_set))
            for a in ans:
                self.assertIn("_".join(map(str, a)), gt_set)


if __name__ == "__main__":
    unittest.main()
