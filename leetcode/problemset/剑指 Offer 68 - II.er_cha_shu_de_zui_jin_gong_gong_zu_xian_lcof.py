#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# https://leetcode.cn/problems/er-cha-shu-de-zui-jin-gong-gong-zu-xian-lcof

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    """与236题相同."""

    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:

        def dfs(node: TreeNode):
            """返回以node为根的子树是否包含p和q."""
            if not node:
                return False, False, None
            left = dfs(node.left)
            right = dfs(node.right)
            if left[2]:
                return left
            if right[2]:
                return right
            ans = [
                node == p or left[0] or right[0],
                node == q or left[1] or right[1],
                None
            ]
            if ans[0] and ans[1]:
                ans[2] = node
            return ans

        return dfs(root)[2]
