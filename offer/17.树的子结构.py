## 题目描述
# 输入两棵二叉树A，B，判断B是不是A的子结构。
# （ps：我们约定空树不是任意一个树的子结构）


# -*- coding:utf-8 -*-
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
class Solution:
    def HasSubtree(self, pRoot1, pRoot2):
        # write code here
        if pRoot2 == None or pRoot1 == None:
            return False
        return self.isSubtree(pRoot1, pRoot2) or self.isSubtree(pRoot1.left, pRoot2) or self.isSubtree(pRoot1.right, pRoot2)
    
    def isSubtree(self, root1, root2):
        if root2 == None:
            return True
        if root1 == None or root1.val != root2.val: # 注意先后顺序
            return False
        return self.isSubtree(root1.left, root2.left) and self.isSubtree(root1.right, root2.right)
