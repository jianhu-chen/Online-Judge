#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# https://leetcode.cn/problems/count-complete-tree-nodes
from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def countNodes(self, root: Optional[TreeNode]) -> int:
        return self.solution2(root)

    def solution1(self, root: Optional[TreeNode]) -> int:
        """dfs."""
        ans = 0

        def dfs(n):
            if not n:
                return
            nonlocal ans
            ans += 1
            dfs(n.left)
            dfs(n.right)

        dfs(root)
        return ans

    def solution2(self, root: Optional[TreeNode]) -> int:
        """二分."""

        level, base = -1, 0
        node = root
        while node:
            level += 1
            base += 2 ** level
            node = node.left
        base -= 2 ** level

        def check(n):
            node = root
            for b in bin(n)[3:]:
                if b == "0":
                    node = node.left
                else:
                    node = node.right
            return node

        ans = 0
        L, R = base + 1, base + 2 ** level
        while L <= R:
            M = L + ((R - L) >> 1)
            if check(M):
                ans = M
                L = M + 1
            else:
                R = M - 1
        return ans
