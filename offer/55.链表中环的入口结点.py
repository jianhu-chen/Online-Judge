## 题目描述
# 给一个链表，若其中包含环，请找出该链表的环的入口结点，否则，输出null。


# -*- coding:utf-8 -*-
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None
class Solution:
    def EntryNodeOfLoop(self, pHead):
        # write code here
        if not pHead:
            return None
        nodes = []
        while pHead != None and pHead not in nodes:
            nodes.append(pHead)
            pHead = pHead.next
        return pHead
