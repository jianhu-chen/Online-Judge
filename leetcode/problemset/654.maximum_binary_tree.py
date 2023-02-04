#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# https://leetcode.cn/problems/maximum-binary-tree
from typing import List, Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def constructMaximumBinaryTree(self, nums: List[int]) -> Optional[TreeNode]:
        def dfs(arr):
            if not arr:
                return None
            max_idx = 0
            for i in range(1, len(arr)):
                if arr[i] > arr[max_idx]:
                    max_idx = i
            left = dfs(arr[:max_idx])
            right = dfs(arr[max_idx + 1:])
            return TreeNode(arr[max_idx], left, right)
        return dfs(nums)
