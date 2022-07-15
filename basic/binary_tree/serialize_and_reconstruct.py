#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import random
import unittest
from typing import List

from utils import Node, random_tree


class SerializeAndReconstruct:

    def serialize_preorder(self, root: Node) -> str:
        if not root:
            return "#"

        preorder = []
        stack: List[Node] = [root]
        while stack:
            node = stack.pop()
            preorder.append(str(node.val) if node else "#")
            if node:
                stack.append(node.right)
                stack.append(node.left)

        return ",".join(preorder)

    def serialize_postorder(self, root: Node) -> str:
        if not root:
            return "#"

        result: List[str] = []
        stack: List[Node] = [root]
        while stack:
            node = stack.pop()
            result.append(str(node.val) if node else "#")
            if node:
                stack.append(node.left)
                stack.append(node.right)

        return ",".join(result[::-1])

    def serialize_level(self, root: Node) -> str:
        if not root:
            return "#"

        result: List[str] = []
        queue: List[Node] = [root]
        while queue:
            node = queue.pop(0)
            result.append(str(node.val) if node else "#")
            if node:
                queue.append(node.left)
                queue.append(node.right)

        return ",".join(result)

    def reconstruct_preorder(self, s: str) -> Node:
        if not s:
            return

        # 中左右进队列 => 中左右出队列
        str_queue: List[str] = s.split(",")

        def process(str_queue: List[str]) -> Node:
            val = str_queue.pop(0)
            if val == "#":
                return None
            node = Node(int(val))
            node.left = process(str_queue)
            node.right = process(str_queue)
            return node

        return process(str_queue)

    def reconstruct_postorder(self, s: str) -> Node:
        if not s:
            return

        # 左右中进栈 => 中左右出栈
        str_stack: List[str] = s.split(",")

        def process(str_stack: List[str]) -> Node:
            val = str_stack.pop()
            if val == "#":
                return None
            node = Node(int(val))
            node.right = process(str_stack)
            node.left = process(str_stack)
            return node

        return process(str_stack)

    def reconstruct_level(self, s: str) -> Node:
        if not s:
            return

        str_queue: List[str] = s.split(",")
        root = Node(int(str_queue.pop(0)))
        node_queue: List[Node] = [root]
        while str_queue:
            val = str_queue.pop(0)
            left = Node(int(val)) if val != "#" else None
            val = str_queue.pop(0)
            right = Node(int(val)) if val != "#" else None

            fa = node_queue.pop(0)
            if left:
                fa.left = left
                node_queue.append(left)
            if right:
                fa.right = right
                node_queue.append(right)

        return root


class Tester(unittest.TestCase):

    def test_solution(self):
        obj = SerializeAndReconstruct()
        for _ in range(1000):
            root = random_tree(height=random.randint(0, 9))
            preorder = obj.serialize_preorder(root)
            ans = obj.reconstruct_preorder(preorder)
            self.assertEqual([n.val for n in root.preorder], [n.val for n in ans.preorder])

            postorder = obj.serialize_postorder(root)
            ans = obj.reconstruct_postorder(postorder)
            self.assertEqual([n.val for n in root.preorder], [n.val for n in ans.preorder])

            level = obj.serialize_level(root)
            ans = obj.reconstruct_level(level)
            self.assertEqual([n.val for n in root.preorder], [n.val for n in ans.preorder])


if __name__ == "__main__":
    root = random_tree(height=random.randint(2, 3))
    obj = SerializeAndReconstruct()
    print(root)
    s = obj.serialize_level(root)
    print(s)
    r = obj.reconstruct_level(s)
    print(r)
    unittest.main()
