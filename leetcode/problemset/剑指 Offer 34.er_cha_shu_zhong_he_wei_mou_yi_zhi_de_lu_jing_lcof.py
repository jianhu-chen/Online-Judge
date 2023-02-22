#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# https://leetcode.cn/problems/er-cha-shu-zhong-he-wei-mou-yi-zhi-de-lu-jing-lcof
from typing import List


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def pathSum(self, root: TreeNode, target: int) -> List[List[int]]:
        ans, path = [], []

        def dfs(node, s):
            if not node:
                return
            s += node.val
            path.append(node.val)
            if s == target and node.left is None and node.right is None:
                ans.append(path.copy())
            dfs(node.left, s)
            dfs(node.right, s)
            path.pop()

        dfs(root, 0)
        return ans
