#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# https://leetcode.cn/problems/reverse-odd-levels-of-binary-tree
from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def reverseOddLevels(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        nodes = []
        queue = [root]
        while queue:
            n = queue.pop(0)
            if n.left:
                queue.append(n.left)
                queue.append(n.right)
            nodes.append(n)

        i = 1  # layer
        while 1:
            s, e = (2 ** i) - 1, (2 ** (i + 1)) - 1
            if s > len(nodes):
                break
            nums = e - s
            nodes[s: s + nums] = nodes[s: s + nums][::-1]
            i += 2

        i = 0  # node
        for i in range(len(nodes)):
            l, r = 2 * i + 1, 2 * i + 2
            if l >= len(nodes):
                break
            nodes[i].left = nodes[l]
            nodes[i].right = nodes[r]

        return root
