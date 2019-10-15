## 题目描述
# 输入两个单调递增的链表，输出两个链表合成后的链表，
# 当然我们需要合成后的链表满足单调不减规则。

# -*- coding:utf-8 -*-
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None
class Solution:
    # 返回合并后列表
    def Merge(self, pHead1, pHead2):
        # write code here
        l = []
        while pHead1 and pHead2:
            if pHead1.val <= pHead2.val:
                l.append(pHead1)
                pHead1 = pHead1.next
            else:
                l.append(pHead2)
                pHead2 = pHead2.next

        while pHead1:
            l.append(pHead1)
            pHead1 = pHead1.next

        while pHead2:
            l.append(pHead2)
            pHead2 = pHead2.next
            
        if l != []:
            head = l[0]
            for i in range(len(l)-1):
                l[i].next = l[i+1]
            l[-1].next = None
            return head
            