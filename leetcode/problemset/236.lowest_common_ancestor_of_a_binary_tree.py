#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# https://leetcode.cn/problems/lowest-common-ancestor-of-a-binary-tree

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        if not root:
            return None

        def process(node):
            """返回(p是否找到, q是否找到, 答案)"""
            if not node:
                return (False, False, None)

            left = process(node.left)
            right = process(node.right)

            find_p = node == p or left[0] or right[0]
            find_q = node == q or left[1] or right[1]
            lcp = None
            if left[2]:
                lcp = left[2]
            elif right[2]:
                lcp = right[2]
            elif find_p and find_q:
                lcp = node
            return (find_p, find_q, lcp)

        return process(root)[2]
