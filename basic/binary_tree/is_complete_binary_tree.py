#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import random
import unittest

from utils import Node, random_tree


class IsCompleteBinaryTree:

    def solution1(self, root: Node) -> bool:
        if not root:
            return True

        queue = [root]
        leaf = False
        while queue:
            node = queue.pop(0)
            if leaf and (node.left is not None or node.right is not None):
                return False
            # case 1: 有右无左
            if node.left is None and node.right is not None:
                return False
            # case 2: 左右孩子不双全
            if node.left is None or node.right is None:
                leaf = True
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
        return True


class Tester(unittest.TestCase):

    def test_solution(self):
        obj = IsCompleteBinaryTree()
        bct_cnt = 0
        for _ in range(10000):
            root = random_tree(height=random.randint(0, 5))
            ans1 = obj.solution1(root)
            bct_cnt += 1 if ans1 else 0
            self.assertEqual(ans1, root.is_complete, root)
        print(f"bct rate: {bct_cnt/10000:.2%}")


if __name__ == "__main__":
    unittest.main()
