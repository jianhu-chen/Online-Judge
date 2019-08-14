## 题目描述
# 从上到下按层打印二叉树，同一层结点从左至右输出。每一层输出一行。

# -*- coding:utf-8 -*-
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
class Solution:
    # 返回二维列表[[1,2],[4,5]]
    def Print(self, pRoot):
        # write code here
        if not pRoot:
            return []
        queue = [pRoot]
        result = []
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
            result.append(row)
        return result
