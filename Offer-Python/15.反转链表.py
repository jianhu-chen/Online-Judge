## 题目描述
# 输入一个链表，反转链表后，输出新链表的表头。

# -*- coding:utf-8 -*-
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None
class Solution:
    # 返回ListNode
    def ReverseList(self, pHead):
        # write code here
        if not pHead or not pHead.next:
            return pHead
        last = None
        while pHead:
            temp = pHead.next
            pHead.next = last
            # last 和 pHead 向前移动
            last = pHead
            pHead = temp
        return last
