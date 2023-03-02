#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# https://leetcode.cn/problems/zhong-jian-er-cha-shu-lcof
from typing import List


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> TreeNode:

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
