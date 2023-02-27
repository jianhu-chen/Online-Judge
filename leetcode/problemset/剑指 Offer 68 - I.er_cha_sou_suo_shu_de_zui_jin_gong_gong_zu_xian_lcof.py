#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# https://leetcode.cn/problems/er-cha-sou-suo-shu-de-zui-jin-gong-gong-zu-xian-lcof

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    """与235题相同."""

    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        if p.val > q.val:
            p, q = q, p
        while True:
            if root.val < p.val:
                root = root.right
            elif root.val > q.val:
                root = root.left
            else:
                return root
