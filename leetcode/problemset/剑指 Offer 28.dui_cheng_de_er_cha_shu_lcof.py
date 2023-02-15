#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# https://leetcode.cn/problems/dui-cheng-de-er-cha-shu-lcof

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def isSymmetric(self, root: TreeNode) -> bool:
        return self.solution1(root)

    def solution1(self, root: TreeNode) -> bool:

        def check(a, b):
            if not a and not b:
                return True
            if not a or not b:
                return False
            return a.val == b.val and check(a.left, b.right) and check(a.right, b.left)

        return check(root, root)

    def solution2(self, root: TreeNode) -> bool:
        """层次遍历."""
        q = [(root, 0)]
        cur_lv, lv_nodes = 0, []
        while q:
            node, lv = q.pop(0)
            if lv == cur_lv:
                lv_nodes.append(node.val if node else None)
            else:
                if lv_nodes != lv_nodes[::-1]:
                    return False
                cur_lv = lv
                lv_nodes = [(node.val if node else None)]
            if node:
                q.append((node.left, lv + 1))
                q.append((node.right, lv + 1))
        if lv_nodes != lv_nodes[::-1]:
            return False
        return True
