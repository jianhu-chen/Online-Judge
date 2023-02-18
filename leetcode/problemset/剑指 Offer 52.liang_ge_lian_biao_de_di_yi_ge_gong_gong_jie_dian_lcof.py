#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# https://leetcode.cn/problems/liang-ge-lian-biao-de-di-yi-ge-gong-gong-jie-dian-lcof

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> ListNode:
        if not headA or not headB:
            return None

        h1, h2 = headA, headB
        cnt = 0
        while h1:
            h1 = h1.next
            cnt += 1
        while h2:
            h2 = h2.next
            cnt -= 1

        if cnt > 0:
            fast, slow = headA, headB
        else:
            fast, slow = headB, headA
            cnt = -cnt

        while cnt:
            fast = fast.next
            cnt -= 1

        while fast != slow and fast:
            fast = fast.next
            slow = slow.next

        return fast
