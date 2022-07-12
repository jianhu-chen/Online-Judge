#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import random
import unittest

from utils import Node, random_tree


class IsFullBinaryTree:

    def solution1(self, root: Node) -> bool:
        if not root:
            return True

        # (noode, level)
        queue = [(root, 0)]
        cur_level = 0
        cur_level_nodes = 0
        while queue:
            node, level = queue.pop(0)
            if level != cur_level:
                if 2 ** cur_level != cur_level_nodes:
                    return False
                cur_level += 1
                cur_level_nodes = 1
            else:
                cur_level_nodes += 1

            if node.left:
                queue.append((node.left, level + 1))
            if node.right:
                queue.append((node.right, level + 1))

        # last level
        if 2 ** cur_level != cur_level_nodes:
            return False

        return True

    def solution2(self, root: Node) -> bool:
        if not root:
            return True

        def process(node):
            """返回是否是完全二叉树以及子树节点个数."""
            if not node:
                return (True, 0)

            left = process(node.left)
            right = process(node.right)

            if left[0] and right[0] and left[1] == right[1]:
                return (True, left[1] + right[1] + 1)
            else:
                return (False, 0)

        return process(root)[0]


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
