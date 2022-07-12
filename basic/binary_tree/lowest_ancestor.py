#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import random
import unittest

from utils import Node, random_tree


class LowestAncestor:

    def solution1(self, root: Node, ch1: Node, ch2: Node) -> Node:
        if not root:
            return

        father = {root: root}
        stack = [root]
        while stack:
            node = stack.pop()
            if node.left:
                father[node.left] = node
                stack.append(node.left)
            if node.right:
                father[node.right] = node
                stack.append(node.right)

        cur = ch1
        ch1_fts = {cur}
        while cur != father[cur]:
            cur = father[cur]
            ch1_fts.add(cur)

        cur = ch2
        while cur not in ch1_fts:
            cur = father[cur]

        return cur

    def solution2(self, root: Node, ch1: Node, ch2: Node) -> Node:
        if not root:
            return

        def process(node):
            """返回三个信息(是否找到ch1, 是否找到ch2, 答案)."""
            if not node:
                return (False, False, None)

            left = process(node.left)
            right = process(node.right)
            find_ch1 = (node == ch1) or left[0] or right[0]
            find_ch2 = (node == ch2) or left[1] or right[1]
            if left[2]:
                ans = left[2]
            elif right[2]:
                ans = right[2]
            elif find_ch1 and find_ch2:
                ans = node
            else:
                ans = None

            return find_ch1, find_ch2, ans

        return process(root)[2]


class Tester(unittest.TestCase):

    def test_solution(self):
        obj = LowestAncestor()
        for _ in range(3000):
            root = random_tree(height=random.randint(0, 9))
            ch1, ch2 = random.choices(root.preorder, k=2)
            ans1 = obj.solution1(root, ch1, ch2)
            ans2 = obj.solution2(root, ch1, ch2)
            self.assertEqual(ans1, ans2, (ch1, ch2, root))


if __name__ == "__main__":
    unittest.main()
