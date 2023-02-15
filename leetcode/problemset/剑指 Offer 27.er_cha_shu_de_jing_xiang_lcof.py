#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# https://leetcode.cn/problems/er-cha-shu-de-jing-xiang-lcof

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def mirrorTree(self, root: TreeNode) -> TreeNode:

        def mirror(node):
            if not node:
                return
            node.left, node.right = node.right, node.left
            mirror(node.left)
            mirror(node.right)

        mirror(root)
        return root
