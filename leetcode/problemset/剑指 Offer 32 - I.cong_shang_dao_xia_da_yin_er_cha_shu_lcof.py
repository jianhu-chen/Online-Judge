#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# https://leetcode.cn/problems/cong-shang-dao-xia-da-yin-er-cha-shu-lcof
from typing import List


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def levelOrder(self, root: TreeNode) -> List[int]:
        q, ans = [root], []
        while q:
            node = q.pop(0)
            if node:
                ans.append(node.val)
                q.append(node.left)
                q.append(node.right)
        return ans
