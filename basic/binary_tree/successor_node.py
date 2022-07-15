#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import random
import unittest
from typing import List

from utils import Node, random_tree


class SuccessorNode:
    """
    有父指针的二叉树, 找到其中一个节点的后继节点.
    """

    def solution1(self, pre: Node) -> Node:
        if not pre:
            return

        root = pre
        while root.parent is not None:
            root = root.parent

        inorder: List[Node] = []
        stack: List[Node] = []
        node = root
        while stack or node:
            while node:
                stack.append(node)
                node = node.left
            node = stack.pop()
            if inorder and inorder[-1] == pre:
                return node
            inorder.append(node)
            node = node.right

        # pre is last node, no successor
        return None

    def solution2(self, pre: Node) -> Node:
        if not pre:
            return

        # case 1: 有右子树, 返回右子树最左的节点
        if pre.right:
            node = pre.right
            while node.left:
                node = node.left
            return node

        # case 2: 没有右子树, 返回第一个父节点是其父节点的右孩子的节点
        else:
            parent = pre.parent
            while parent and parent.right == pre:
                pre = parent
                parent = pre.parent
            return parent


class Tester(unittest.TestCase):

    def test_solution(self):
        obj = SuccessorNode()
        for _ in range(3000):
            root = random_tree(height=random.randint(0, 9))
            preorder = root.preorder
            for fa in preorder:
                if not hasattr(fa, "parent"):
                    setattr(fa, "parent", None)
                if fa.left:
                    fa.left.parent = fa
                if fa.right:
                    fa.right.parent = fa
            pre = random.choice(preorder)
            ans1 = obj.solution1(pre)
            ans2 = obj.solution2(pre)
            self.assertEqual(ans1, ans2, (root, ans1, ans2))


if __name__ == "__main__":
    unittest.main()
