#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import random
import unittest
from queue import Queue
from utils import Node, random_tree


class TreeMaxWidth:

    def solution1(self, root: Node) -> int:
        if not root:
            return 0

        max_width = 1
        queue = Queue()
        queue.put((root, 1))  # (node, level)
        cur_level = 1
        cur_level_nodes = 0
        while not queue.empty():
            node, node_level = queue.get()
            if node_level == cur_level:
                cur_level_nodes += 1
            else:
                max_width = max(max_width, cur_level_nodes)
                cur_level_nodes = 1
                cur_level += 1
            if node.left:
                queue.put((node.left, node_level + 1))
            if node.right:
                queue.put((node.right, node_level + 1))
        # !NOTE (jianhu): last level
        max_width = max(max_width, cur_level_nodes)
        return max_width

    def solution2(self, root: Node) -> int:
        if not root:
            return 0

        cur_level_end_node = root
        next_level_end_node = None
        cur_level = 1
        cur_level_nodes = 0
        max_width = 1
        queue = Queue()
        queue.put(root)
        while not queue.empty():
            node = queue.get()
            cur_level_nodes += 1

            for child in (node.left, node.right):
                if child is not None:
                    queue.put(child)
                    next_level_end_node = child

            if node == cur_level_end_node:
                max_width = max(max_width, cur_level_nodes)
                cur_level_end_node = next_level_end_node
                cur_level_nodes = 0
                cur_level += 1

        return max_width


class Tester(unittest.TestCase):

    def test_solution(self):
        obj = TreeMaxWidth()
        for _ in range(1000):
            root = random_tree(height=random.randint(0, 9))
            ans1 = obj.solution1(root)
            ans2 = obj.solution2(root)
            self.assertEqual(ans1, ans2, root)


if __name__ == "__main__":
    unittest.main()
