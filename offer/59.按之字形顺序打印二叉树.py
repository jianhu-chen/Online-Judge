## 题目描述
# 请实现一个函数按照之字形打印二叉树，即第一行按照从左到右的顺序打印，
# 第二层按照从右至左的顺序打印，第三行按照从左到右的顺序打印，其他行以此类推。

# -*- coding:utf-8 -*-
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
class Solution:
    def Print(self, pRoot):
        # write code here
        if not pRoot:
            return []
        queue = [pRoot]
        result = []
        flag = True # left -> right
        while queue:
            row = []
            n = len(queue)
            for _ in range(n):    
                node = queue.pop()
                row.append(node.val)
                if node.left:
                    queue.insert(0, node.left)
                if node.right:
                    queue.insert(0, node.right)
            if flag:
                result.append(row)
            else:
                result.append(row[::-1])
            flag = not flag
        return result
