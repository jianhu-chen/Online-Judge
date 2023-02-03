#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# https://leetcode.cn/problems/reverse-nodes-in-k-group
from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        # 先求链表长度
        n, cur = 0, head
        while cur:
            n += 1
            cur = cur.next

        dummy = ListNode(next=head)
        p0 = dummy
        while n >= k:
            n -= k
            pre, cur, nxt = None, p0.next, None
            for _ in range(k):
                nxt = cur.next
                cur.next = pre
                pre = cur
                cur = nxt

            nxt = p0.next
            p0.next.next = cur
            p0.next = pre
            p0 = nxt

        return dummy.next
