#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# https://leetcode.cn/problems/cousins-in-binary-tree-ii
from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def replaceValueInTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        # 1. 把下一排的值加起来
        # 2. 更新左右儿子的节点
        root.val = 0
        q = [root]
        while q:
            tmp = q
            q = []
            s = 0
            for x in tmp:
                if x.left:
                    s += x.left.val
                    q.append(x.left)
                if x.right:
                    s += x.right.val
                    q.append(x.right)
            for x in tmp:
                val = s - (x.left.val if x.left else 0) - (x.right.val if x.right else 0)
                if x.left:
                    x.left.val = val
                if x.right:
                    x.right.val = val
        return root
