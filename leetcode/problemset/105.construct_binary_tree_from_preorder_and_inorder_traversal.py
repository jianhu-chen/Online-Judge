#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# https://leetcode.cn/problems/construct-binary-tree-from-preorder-and-inorder-traversal
from typing import List, Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:

        def dfs(pre, ino):
            if not pre:
                return None
            if len(pre) == 1:
                return TreeNode(pre[0])
            val = pre[0]
            node = TreeNode(pre[0])
            idx = ino.index(val)
            node.left = dfs(pre[1:idx + 1], ino[0:idx])
            node.right = dfs(pre[idx + 1:], ino[idx + 1:])
            return node

        return dfs(preorder, inorder)
