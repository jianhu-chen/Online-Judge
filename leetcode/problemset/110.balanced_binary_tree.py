#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# https://leetcode.cn/problems/balanced-binary-tree
from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return True

        def process(node):
            """返回信息(是否为平衡二叉树, 高度)"""
            if not node:
                return (True, 0)

            left = process(node.left)
            right = process(node.right)
            if left[0] and right[0] and abs(left[1] - right[1]) <= 1:
                return (True, max(left[1], right[1]) + 1)

            return (False, 0)

        return process(root)[0]
