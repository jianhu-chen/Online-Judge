# -*- encoding: utf-8 -*-
'''
@File    :   100.same-tree.py
@Time    :   2019/11/17 22:22:52
@Author  :   jhchen
@E-mail  :   jianhuchen@163.com
@License :   Copyright(C), USTC
@Desc    :   None
'''
#
# @lc app=leetcode id=100 lang=python
#
# [100] Same Tree
#
# https://leetcode.com/problems/same-tree/description/
#
# algorithms
# Easy (51.09%)
# Likes:    1439
# Dislikes: 46
# Total Accepted:    444.4K
# Total Submissions: 868K
# Testcase Example:  '[1,2,3]\n[1,2,3]'
#
# Given two binary trees, write a function to check if they are the same or
# not.
#
# Two binary trees are considered the same if they are structurally identical
# and the nodes have the same value.
#
# Example 1:
#
#
# Input:     1         1
# ⁠         / \       / \
# ⁠        2   3     2   3
#
# ⁠       [1,2,3],   [1,2,3]
#
# Output: true
#
#
# Example 2:
#
#
# Input:     1         1
# ⁠         /           \
# ⁠        2             2
#
# ⁠       [1,2],     [1,null,2]
#
# Output: false
#
#
# Example 3:
#
#
# Input:     1         1
# ⁠         / \       / \
# ⁠        2   1     1   2
#
# ⁠       [1,2,1],   [1,1,2]
#
# Output: false
#
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
    def isSameTree(self, p, q):
        """
        :type p: TreeNode
        :type q: TreeNode
        :rtype: bool
        """
        p_LDR_list = []
        q_LDR_list = []
        self.getLDRList(p, p_LDR_list)
        self.getLDRList(q, q_LDR_list)

        if len(p_LDR_list) != len(q_LDR_list):
            return False

        for i, j in zip(p_LDR_list, q_LDR_list):
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
# @lc code=end
