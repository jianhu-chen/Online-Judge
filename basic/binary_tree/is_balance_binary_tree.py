#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import random
import unittest

from utils import Node, random_tree


class IsBinanceBinaryTree:

    def solution(self, root: Node) -> bool:
        if not root:
            return True

        def process(node):
            """返回是否是平衡二叉树以及子树高度."""
            if not node:
                return (True, 0)

            left = process(node.left)
            right = process(node.right)

            if left[0] and right[0] and abs(left[1] - right[1]) <= 1:
                return (True, max(left[1], right[1]) + 1)

            return (False, 0)

        return process(root)[0]


class Tester(unittest.TestCase):

    def test_solution(self):
        obj = IsBinanceBinaryTree()
        bst_cnt = 0
        for _ in range(5000):
            root = random_tree(height=random.randint(0, 9))
            ans = obj.solution(root)
            gt = root.is_balanced
            bst_cnt += 1 if gt else 0
            self.assertEqual(ans, gt, root)
        print(f"bbt rate: {bst_cnt/5000:.2%}")


if __name__ == "__main__":
    unittest.main()
