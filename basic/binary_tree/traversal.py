#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import random
import unittest
from typing import List

from utils import Node, random_tree


class PreOrderTraversal:

    def solution1(self, root: Node) -> List[Node]:
        """递归实现."""
        if not root:
            return []

        left = self.solution1(root.left)
        right = self.solution1(root.right)
        return [root] + left + right

    def solution2(self, root: Node) -> List[Node]:
        """迭代实现."""
        if not root:
            return []

        stack = [root]
        result = []
        while stack:
            node = stack.pop()
            result.append(node)
            if node.right is not None:
                stack.append(node.right)
            if node.left is not None:
                stack.append(node.left)
        return result


class InOrderTraversal:

    def solution1(self, root: Node) -> List[Node]:
        """递归实现."""
        if not root:
            return []

        left = self.solution1(root.left)
        right = self.solution1(root.right)
        return left + [root] + right

    def solution2(self, root: Node) -> List[Node]:
        """迭代实现."""
        if not root:
            return []

        stack = []
        result = []
        node = root
        while stack or node:
            while node:
                stack.append(node)
                node = node.left
            node = stack.pop()
            result.append(node)
            node = node.right
        return result


class PostOrderTraversal:

    def solution1(self, root: Node) -> List[Node]:
        """递归实现."""
        if not root:
            return []

        left = self.solution1(root.left)
        right = self.solution1(root.right)
        return left + right + [root]

    def solution2(self, root: Node) -> List[Node]:
        """迭代实现.

        1. 根节点进栈
        2. 顶部节点出栈, 若非空, 入收集栈, 将左右孩子进栈
        3. 重复操作知道栈空
        """
        if not root:
            return []

        stack = [root]
        result = []
        while stack:
            node = stack.pop()
            result.append(node)
            if node.left is not None:
                stack.append(node.left)
            if node.right is not None:
                stack.append(node.right)
        return result[::-1]


class LevelTraversal:

    def solution(self, root: Node) -> List[Node]:
        if not root:
            return []

        result = []
        queue = [root]
        while queue:
            node = queue.pop(0)
            result.append(node)
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
        return result


class Tester(unittest.TestCase):

    def test_pre_order_traversal(self):
        obj = PreOrderTraversal()
        for _ in range(1000):
            root = random_tree(height=random.randint(0, 9))
            gt = root.preorder
            ans = obj.solution1(root)
            self.assertEqual(gt, ans)
            ans = obj.solution2(root)
            self.assertEqual(gt, ans)

    def test_in_order_traversal(self):
        obj = InOrderTraversal()
        for _ in range(1000):
            root = random_tree(height=random.randint(0, 9))
            gt = root.inorder
            ans = obj.solution1(root)
            self.assertEqual(gt, ans)
            ans = obj.solution2(root)
            self.assertEqual(gt, ans)

    def test_post_order_traversal(self):
        obj = PostOrderTraversal()
        for _ in range(1000):
            root = random_tree(height=random.randint(0, 9))
            gt = root.postorder
            ans = obj.solution1(root)
            self.assertEqual(gt, ans)
            ans = obj.solution2(root)
            self.assertEqual(gt, ans)

    def test_level_traversal(self):
        obj = LevelTraversal()
        for _ in range(1000):
            root = random_tree(height=random.randint(0, 9))
            gt = root.levelorder
            ans = obj.solution(root)
            self.assertEqual(gt, ans)


if __name__ == "__main__":
    unittest.main()
