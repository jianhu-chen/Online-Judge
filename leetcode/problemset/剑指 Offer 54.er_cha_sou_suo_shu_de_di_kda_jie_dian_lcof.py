#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# https://leetcode.cn/problems/er-cha-sou-suo-shu-de-di-kda-jie-dian-lcof

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def kthLargest(self, root: TreeNode, k: int) -> int:
        def dfs(node):
            if not node:
                return
            right = dfs(node.right)
            nonlocal k
            k -= 1
            if k == 0:
                return node.val
            left = dfs(node.left)
            return left or right

        return dfs(root)
