#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# https://leetcode.cn/problems/diameter-of-binary-tree
from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        def process(node):
            """返回子树的高度和最大直径."""
            if not node:
                return 0, 0
            left = process(node.left)
            right = process(node.right)
            x1 = left[0] + right[0]
            x2 = max(left[1], right[1])
            return max(left[0], right[0]) + 1, max(x1, x2)
        return process(root)[1]
