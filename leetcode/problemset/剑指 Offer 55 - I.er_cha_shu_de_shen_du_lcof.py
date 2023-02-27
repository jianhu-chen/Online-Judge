#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# https://leetcode.cn/problems/er-cha-shu-de-shen-du-lcof

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def maxDepth(self, root: TreeNode) -> int:

        def dfs(node):
            if not node:
                return 0
            return max(dfs(node.left), dfs(node.right)) + 1

        return dfs(root)
