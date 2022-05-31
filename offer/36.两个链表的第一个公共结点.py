## 题目描述
# 输入两个链表，找出它们的第一个公共结点。

# -*- coding:utf-8 -*-
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None
class Solution:
    def FindFirstCommonNode(self, pHead1, pHead2):
        # write code here
        if not pHead1 or not pHead2:
            return None
        stack1 = []
        stack2 = []
        while pHead1 != None:
            stack1.append(pHead1)
            pHead1 = pHead1.next
        while pHead2 != None:
            stack2.append(pHead2)
            pHead2 = pHead2.next
        result = None
        while True:
            if stack1==[] or stack2==[]:
                return result
            n1 = stack1.pop()
            n2 = stack2.pop()
            if n1 == n2:
                result = n1
            else:
                break
        return result
                
        