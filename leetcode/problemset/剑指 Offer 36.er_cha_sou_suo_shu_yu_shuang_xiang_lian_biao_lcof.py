#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# https://leetcode.cn/problems/er-cha-sou-suo-shu-yu-shuang-xiang-lian-biao-lcof

# Definition for a Node.
class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def treeToDoublyList(self, root: 'Node') -> 'Node':
        if not root:
            return
        if not root.left and not root.right:
            root.left = root
            root.right = root
            return root

        def inorder(node):
            if not node:
                return []
            left = inorder(node.left)
            right = inorder(node.right)
            return left + [node] + right

        nodes = inorder(root)
        for i in range(1, len(nodes) - 1):
            nodes[i].left = nodes[i - 1]
            nodes[i].right = nodes[i + 1]

        nodes[0].left = nodes[-1]
        nodes[0].right = nodes[1]
        nodes[-1].left = nodes[-2]
        nodes[-1].right = nodes[0]
        return nodes[0]
