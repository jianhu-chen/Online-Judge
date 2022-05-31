## 题目描述
# 输入一个链表，输出该链表中倒数第k个结点。

# -*- coding:utf-8 -*-
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def FindKthToTail(self, head, k):
        # write code here
        if not head:
            return 
        val_list = []
        p = head
        while p:
            val_list.append(p)
            p = p.next
        if k < 1 or k > len(val_list):
            return 
        else:
            return val_list[-k]

