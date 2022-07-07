#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import random
import unittest

from utils import Node, random_bst, random_tree


class IsBinarySearchTree:

    def solution1(self, root: Node) -> bool:
        if not root:
            return True

        pre_val = -float("inf")  # 中序遍历前一个节点的值
        stack = []
        node = root
        while stack or node:
            while node:
                stack.append(node)
                node = node.left
            node = stack.pop()
            if node.val <= pre_val:
                return False
            pre_val = node.val
            node = node.right
        return True

    def solution2(self, root: Node) -> bool:
        if not root:
            return True

        def process(node: Node):
            """返回三个信息: (是否为bst, 最大值, 最小值)"""
            if not node:
                return None

            left = process(node.left)
            right = process(node.right)
            max_val, min_val = node.val, node.val
            is_bst = True
            if left is not None:
                min_val = left[2]
                if not left[0] or left[1] >= node.val:
                    is_bst = False
            if right is not None:
                max_val = right[1]
                if not right[0] or right[2] <= node.val:
                    is_bst = False
            return (is_bst, max_val, min_val)

        return process(root)[0]


class Tester(unittest.TestCase):

    def test_solution(self):
        obj = IsBinarySearchTree()
        bst_cnt = 0
        for _ in range(1000):
            if random.random() < 0.6:
                root = random_tree(height=random.randint(0, 9))
            else:
                root = random_bst(height=random.randint(0, 9))
            ans1 = obj.solution1(root)
            ans2 = obj.solution2(root)
            bst_cnt += 1 if ans1 else 0
            self.assertEqual(ans1, ans2, root)
        print(f"bst rate: {bst_cnt/1000:.2%}")


if __name__ == "__main__":
    unittest.main()
