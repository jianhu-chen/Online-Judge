#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# https://leetcode.cn/problems/cong-shang-dao-xia-da-yin-er-cha-shu-iii-lcof
from typing import List


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        q, ans = [(root, 0)], []
        while q:
            node, lv = q.pop(0)
            if node:
                if len(ans) == lv:
                    ans.append([node.val])
                elif lv & 1:
                    ans[-1].insert(0, node.val)
                else:
                    ans[-1].append(node.val)
                q.append((node.left, lv + 1))
                q.append((node.right, lv + 1))
        return ans
