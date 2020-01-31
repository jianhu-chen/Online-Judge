# -*- encoding: utf-8 -*-
'''
@File    :   235.lowest-common-ancestor-of-a-binary-search-tree.py
@Time    :   2020/01/31 18:48:59
@Author  :   jhchen
@E-mail  :   jianhuchen@163.com
@License :   Copyright(C), USTC
@Desc    :   None
'''
#
# @lc app=leetcode id=235 lang=python
#
# [235] Lowest Common Ancestor of a Binary Search Tree
#

# @lc code=start
# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    # def lowestCommonAncestor(self, root, p, q):
    #     """方法一：递归
    #     算法:
    #         1. 从根节点开始遍历树
    #         2. 如果节点 pp 和节点 qq 都在右子树上，那么以右孩子为根节点继续 1 的操作
    #         3. 如果节点 pp 和节点 qq 都在左子树上，那么以左孩子为根节点继续 1 的操作
    #         4. 如果条件 2 和条件 3 都不成立，这就意味着我们已经找到节 pp 和节点 qq 的 LCA 了
    #     :type root: TreeNode
    #     :type p: TreeNode
    #     :type q: TreeNode
    #     :rtype: TreeNode
    #     """
    #     root_val = root.val
    #     p_val = p.val
    #     q_val = q.val
    #     if root_val > p_val and root_val > q_val:
    #         return self.lowestCommonAncestor(root.left, p, q)
    #     elif root_val < p_val and root_val < q_val:
    #         return self.lowestCommonAncestor(root.right, p, q)
    #     else:
    #         return root

    def lowestCommonAncestor(self, root, p, q):
        """方法二：迭代
        :type root: TreeNode
        :type p: TreeNode
        :type q: TreeNode
        :rtype: TreeNode
        """
        p_val = p.val
        q_val = q.val
        while root:
            root_val = root.val
            if root_val > p_val and root_val > q_val:
                root = root.left
            elif root_val < p_val and root_val < q_val:
                root = root.right
            else:
                return root
# @lc code=end

