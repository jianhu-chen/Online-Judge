#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# https://leetcode.cn/problems/add-two-numbers
from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:

    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        return self.addTwoNumbers1(l1, l2)

    def addTwoNumbers1(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        pre = head = ListNode(0, None)
        carry = False
        while l1 or l2 or carry:
            val = 0
            if l1:
                val += l1.val
            if l2:
                val += l2.val
            if carry:
                val += 1
            carry = val >= 10
            pre.next = ListNode(val % 10, None)
            pre = pre.next
            if l1:
                l1 = l1.next
            if l2:
                l2 = l2.next
        return head.next

    def addTwoNumbers2(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        def get_value(li):
            n = 0
            bit = 1
            while li:
                n = n + li.val * bit
                li = li.next
                bit *= 10
            return n

        n1 = get_value(l1)
        n2 = get_value(l2)
        n = n1 + n2

        pre = head = ListNode(0, None)
        while n:
            pre.next = ListNode(val=n % 10, next=None)
            pre = pre.next
            n //= 10
        return head.next if pre != head else head
