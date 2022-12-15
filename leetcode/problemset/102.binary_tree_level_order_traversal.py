#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# https://leetcode.cn/problems/binary-tree-level-order-traversal
from typing import List, Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []

        queue = [(root, 0)]
        ans = []
        cur_level = -1
        while len(queue):
            (node, level) = queue.pop(0)
            if level != cur_level:
                ans.append([node.val])
                cur_level = level
            else:
                ans[level].append(node.val)
            if node.left is not None:
                queue.append((node.left, level + 1))
            if node.right is not None:
                queue.append((node.right, level + 1))
        return ans
