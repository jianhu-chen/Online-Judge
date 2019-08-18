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
        self.mirror_dlr_list = []

    def isSymmetrical(self, pRoot):
        # write code here
        self.getDLRList(pRoot, is_mirror=False) # 获得原树的前序遍历列表
        self.getMirrorTree(pRoot)
        self.getDLRList(pRoot, is_mirror=True) # 获得镜像树的前序遍历列表
        if ''.join(self.dlr_list) == ''.join(self.mirror_dlr_list):
            return True
        else:
            return False

    def getDLRList(self, pRoot, is_mirror):
        if is_mirror:
            l = self.mirror_dlr_list
        else:
            l = self.dlr_list
        if not pRoot:
            l.append('#')
            return
        l.append(str(pRoot.val))
        self.getDLRList(pRoot.left, is_mirror)
        self.getDLRList(pRoot.right, is_mirror)

    def getMirrorTree(self, pRoot):
        if not pRoot:
            return pRoot
        pRoot.left, pRoot.right = pRoot.right, pRoot.left
        if pRoot.left:
            self.getMirrorTree(pRoot.left)
        if pRoot.right:
            self.getMirrorTree(pRoot.right)
        return pRoot

