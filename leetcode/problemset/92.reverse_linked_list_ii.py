#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# https://leetcode.cn/problems/reverse-linked-list-ii
from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        # 哨兵节点
        dummy = ListNode(next=head)
        p0 = dummy
        for _ in range(left - 1):
            p0 = p0.next

        pre, cur, nxt = None, p0.next, None
        for _ in range(right - left + 1):
            nxt = cur.next
            cur.next = pre
            pre = cur
            cur = nxt

        p0.next.next = cur
        p0.next = pre

        return dummy.next
