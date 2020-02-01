# -*- encoding: utf-8 -*-
'''
@File    :   257.binary-tree-paths.py
@Time    :   2020/01/31 19:04:17
@Author  :   jhchen
@E-mail  :   jianhuchen@163.com
@License :   Copyright(C), USTC
@Desc    :   None
'''
#
# @lc app=leetcode id=257 lang=python
#
# [257] Binary Tree Paths
#

# @lc code=start
# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def binaryTreePaths(self, root):
        """
        :type root: TreeNode
        :rtype: List[str]
        """
        if not root:
            return []
        self.result = list()
        self.DFS(root, [])
        self.result = ["->".join(p) for p in self.result]
        return self.result

    def DFS(self, root, path):
        if not root.left and not root.right:
            self.result.append(path + [str(root.val)])
            return
       
        if root.left:
            self.DFS(root.left, path + [str(root.val)])

        if root.right:
            self.DFS(root.right, path + [str(root.val)])
# @lc code=end

