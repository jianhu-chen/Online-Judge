#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# https://leetcode.cn/problems/he-bing-liang-ge-pai-xu-de-lian-biao-lcof

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        dummy = p = ListNode(0)
        while l1 and l2:
            if l1.val <= l2.val:
                p.next = l1
                l1 = l1.next
            else:
                p.next = l2
                l2 = l2.next
            p = p.next

        while l1:
            p.next = l1
            l1 = l1.next
            p = p.next

        while l2:
            p.next = l2
            l2 = l2.next
            p = p.next

        return dummy.next
