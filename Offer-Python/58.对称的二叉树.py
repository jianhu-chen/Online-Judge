## 题目描述
# 请实现一个函数，用来判断一颗二叉树是不是对称的。
# 注意，如果一个二叉树同此二叉树的镜像是同样的，定义其为对称的。

# -*- coding:utf-8 -*-
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
class Solution:
    def __init__(self):
        self.dlr_list = []
        self.sym_dlr_list = []

    def isSymmetrical(self, pRoot):
        # write code here
        self.getDLRList(pRoot) # 获得原树的前序遍历列表


    def getDLRList(self, pHead):
        if not pHead:
            self.dlr_list.append('NULL')
        self.dlr_list.append(pHead)
        self.getDLRList(pHead.left)
        self.getDLRList(pHead.right)
    
    def t