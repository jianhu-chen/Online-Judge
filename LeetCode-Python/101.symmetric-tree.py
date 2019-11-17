# -*- encoding: utf-8 -*-
'''
@File    :   101.symmetric-tree.py
@Time    :   2019/11/17 22:26:12
@Author  :   jhchen
@E-mail  :   jianhuchen@163.com
@License :   Copyright(C), USTC
@Desc    :   None
'''
#
# @lc app=leetcode id=101 lang=python
#
# [101] Symmetric Tree
#
# https://leetcode.com/problems/symmetric-tree/description/
#
# algorithms
# Easy (44.82%)
# Likes:    2859
# Dislikes: 66
# Total Accepted:    496K
# Total Submissions: 1.1M
# Testcase Example:  '[1,2,2,3,4,4,3]'
#
# Given a binary tree, check whether it is a mirror of itself (ie, symmetric
# around its center).
#
# For example, this binary tree [1,2,2,3,4,4,3] is symmetric:
#
#
# ⁠   1
# ⁠  / \
# ⁠ 2   2
# ⁠/ \ / \
# 3  4 4  3
#
#
#
#
# But the following [1,2,2,null,3,null,3] is not:
#
#
# ⁠   1
# ⁠  / \
# ⁠ 2   2
# ⁠  \   \
# ⁠  3    3
#
#
#
#
# Note:
# Bonus points if you could solve it both recursively and iteratively.
#
#

# @lc code=start
# Definition for a binary tree node.


class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    def isSymmetric(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        origin = []
        symmetric = []

        self.getLDRList(root, origin)
        self.setSymmetic(root)
        self.getLDRList(root, symmetric)

        if len(origin) != len(symmetric):
            return False
        for i, j in zip(origin, symmetric):
            if i != j:
                return False
        return True

    def getLDRList(self, pHead, result):
        if not pHead:
            result.append(None)
            return
        result.append(pHead.val)
        self.getLDRList(pHead.left, result)
        self.getLDRList(pHead.right, result)

    def setSymmetic(self, root):
        if not root:
            return
        root.left, root.right = root.right, root.left
        self.setSymmetic(root.left)
        self.setSymmetic(root.right)

# @lc code=end
