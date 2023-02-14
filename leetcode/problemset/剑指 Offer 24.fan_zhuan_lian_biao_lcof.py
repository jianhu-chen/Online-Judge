#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# https://leetcode.cn/problems/fan-zhuan-lian-biao-lcof

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        if not head or not head.next:
            return head

        pre = nxt = None
        while head:
            nxt = head.next
            head.next = pre
            pre = head
            head = nxt
        return pre
