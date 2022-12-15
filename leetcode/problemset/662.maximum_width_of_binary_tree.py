#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# https://leetcode.cn/problems/maximum-width-of-binary-tree
from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def widthOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        nodes = [(root, 1)]
        ans = 0
        while nodes:
            tmp = []
            for node, index in nodes:
                if node.left:
                    tmp.append((node.left, 2 * index))
                if node.right:
                    tmp.append((node.right, 2 * index + 1))
            ans = max(ans, nodes[-1][1] - nodes[0][1] + 1)
            nodes = tmp
        return ans
