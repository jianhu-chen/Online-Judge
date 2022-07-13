#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import unittest
from typing import List


class PaperFolding:
    """
    一张纸条竖直摆放, 每次由下向上折叠, 可以形成如下折痕:
    1次: 凹
    2次: 凹 凹 凸
    3次: 凹 凹 凸 凹 凹 凸 凸
    ...
    请返回折n次后的纸条折痕, 用一个列表表示折痕的方向是凹(0)还是凸(1).
    """

    def solution(self, n: int) -> List[int]:
        if n == 0:
            return []

        def process(i, direction):
            if i > n:
                return []

            left = process(i + 1, 0)  # 凹
            right = process(i + 1, 1)  # 凸
            return left + [direction] + right

        return process(1, 0)


class Tester(unittest.TestCase):

    def test_solution(self):
        obj = PaperFolding()
        n = 0
        self.assertEqual(obj.solution(n), [])
        n = 1
        self.assertEqual(obj.solution(n), [0])
        n = 2
        self.assertEqual(obj.solution(n), [0, 0, 1])
        n = 3
        self.assertEqual(obj.solution(n), [0, 0, 1, 0, 0, 1, 1])


if __name__ == "__main__":
    unittest.main()
