#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import random
import unittest
from typing import List


class ReverseStackUsingRecursive:
    """给定一个栈，请逆序这个栈，不能申请额外的数据结构，只能使用递归函数"""

    def solution(self, stack: List[int]) -> List[int]:
        self.reverse(stack)

    def reverse(self, stack: List[int]) -> List[int]:
        if not stack:
            return
        last = self.extract_last(stack)
        self.reverse(stack)
        stack.append(last)

    def extract_last(self, stack: List[int]) -> int:
        top = stack.pop()
        if not stack:  # empty
            return top
        else:
            last = self.extract_last(stack)
            stack.append(top)
            return last


class Tester(unittest.TestCase):

    def test_solution(self):
        obj = ReverseStackUsingRecursive()
        for _ in range(1000):
            stack = [random.randint(0, 100) for _ in range(random.randint(0, 100))]
            gt = stack[::-1]
            obj.solution(stack)
            self.assertEqual(gt, stack)


if __name__ == "__main__":
    unittest.main()
