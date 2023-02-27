#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# https://leetcode.cn/problems/ping-heng-er-cha-shu-lcof

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def isBalanced(self, root: TreeNode) -> bool:
        """与110题相同."""

        def dfs(node):
            """返回以node为根的子树是否为平衡二叉树以及该子树的深度."""
            if not node:
                return True, 0
            left = dfs(node.left)
            right = dfs(node.right)
            if not left[0] or not right[0]:
                return False, -1
            if abs(left[1] - right[1]) > 1:
                return False, -1
            return True, max(left[1], right[1]) + 1

        return dfs(root)[0]
