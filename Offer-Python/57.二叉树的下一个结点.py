## 题目描述
# 给定一个二叉树和其中的一个结点，请找出中序遍历顺序的下一个结点并且返回。
# 注意，树中的结点不仅包含左右子结点，同时包含指向父结点的指针。

# -*- coding:utf-8 -*-
class TreeLinkNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
        self.next = None
class Solution:
    def __init__(self):
        self.ldr_list = []
        
    def GetNext(self, pNode):
        # write code here
        pHead = pNode
        while pHead.next:
            pHead = pHead.next   
        self.GetLDRList(pHead)
        try:
            return self.ldr_list[self.ldr_list.index(pNode)+1]
        except:
            return None
        
    def GetLDRList(self, pHead):
        if not pHead:
            return
        self.GetLDRList(pHead.left)
        self.ldr_list.append(pHead)
        self.GetLDRList(pHead.right)