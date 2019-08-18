## 题目描述
# 输入一棵二叉树，判断该二叉树是否是平衡二叉树。

# -*- coding:utf-8 -*-
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

# 方法一：自顶向下
# 运行时间：25ms
# 占用内存：5860k
# class Solution:
#     def IsBalanced_Solution(self, pRoot):
#         # write code here
#         if not pRoot:
#             return True
#         left_deep = self.GetDeep(pRoot.left)
#         right_deep = self.GetDeep(pRoot.right)
#         if abs(left_deep - right_deep) > 1:
#             return False
#         else:
#             return self.IsBalanced_Solution(pRoot.left) and self.IsBalanced_Solution(pRoot.right)

#     def GetDeep(self, pRoot):
#         if not pRoot:
#             return 0
#         return max(self.GetDeep(pRoot.left), self.GetDeep(pRoot.right)) + 1
        
# 方法二：自下向上
# 运行时间：22ms
# 占用内存：5852k
class Solution:
    def IsBalanced_Solution(self, pRoot):
        # write code here
        if not pRoot:
            return True
        if self.IsBalanced_Solution(pRoot.left) and self.IsBalanced_Solution(pRoot.right):
            left_deep = self.GetDeep(pRoot.left)
            right_deep = self.GetDeep(pRoot.right)
            if abs(left_deep - right_deep) <= 1:
                return True
            return False

    def GetDeep(self, pRoot):
        if not pRoot:
            return 0
        return max(self.GetDeep(pRoot.left), self.GetDeep(pRoot.right)) + 1