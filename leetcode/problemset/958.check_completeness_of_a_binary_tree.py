#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# https://leetcode.cn/problems/check-completeness-of-a-binary-tree
from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isCompleteTree(self, root: Optional[TreeNode]) -> bool:
        """
        思路:
        1) 有右无左, 返回False
        2) 第一次遇到左右不双全之后的所有节点都是叶结点, 否则返回False
        """
        queue = [root]
        leaf = False
        while queue:
            node = queue.pop(0)
            left_exists = node.left is not None
            right_exists = node.right is not None
            if leaf and (left_exists or right_exists):
                return False
            if not left_exists and right_exists:
                return False
            if not left_exists or not right_exists:
                leaf = True
            if left_exists:
                queue.append(node.left)
            if right_exists:
                queue.append(node.right)
        return True
