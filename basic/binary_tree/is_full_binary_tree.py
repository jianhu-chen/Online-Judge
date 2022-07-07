#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import random
import unittest

from utils import Node, random_tree


class IsFullBinaryTree:

    def solution1(self, root: Node) -> bool:
        if not root:
            return True
        pass

    def solution2(self, root: Node) -> bool:
        if not root:
            return True
        pass


class Tester(unittest.TestCase):

    def test_solution(self):
        obj = IsFullBinaryTree()
        fbt_cnt = 0
        for _ in range(1000):
            is_perfect = True if random.random() > 0.6 else False
            root = random_tree(height=random.randint(0, 9), is_perfect=is_perfect)
            ans1 = obj.solution1(root)
            ans2 = obj.solution2(root)
            fbt_cnt += 1 if ans1 else 0
            self.assertEqual(ans1, ans2, root)
        print(f"fbt rate: {fbt_cnt/1000:.2%}")


if __name__ == "__main__":
    unittest.main()
