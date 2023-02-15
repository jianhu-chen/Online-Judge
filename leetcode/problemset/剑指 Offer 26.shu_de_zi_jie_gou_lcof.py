#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# https://leetcode.cn/problems/shu-de-zi-jie-gou-lcof

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def isSubStructure(self, A: TreeNode, B: TreeNode) -> bool:

        def compare(a, b):
            if not b:
                return True
            if not a:
                return False
            if a.val != b.val:
                return False
            return compare(a.left, b.left) and compare(a.right, b.right)

        def isSub(a, b):
            """判断b是否为a的子树."""
            if not a or not b:
                return False
            return compare(a, b) or isSub(a.left, b) or isSub(a.right, b)

        return isSub(A, B)
