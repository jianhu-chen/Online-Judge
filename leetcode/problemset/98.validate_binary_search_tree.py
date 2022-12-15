#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# https://leetcode.cn/problems/validate-binary-search-tree
from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        """思路: 中序遍历判断是否升序"""
        prev = -float("inf")
        stack = []
        node = root
        while stack and node:
            while node:
                stack.append(node)
                node = node.left
            node = stack.pop()
            if node.val < prev:
                return False
            prev = node.val
            node = node.right
        return True
