#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# https://leetcode.cn/problems/shan-chu-lian-biao-de-jie-dian-lcof

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def deleteNode(self, head: ListNode, val: int) -> ListNode:
        dummy = p = ListNode(0)
        dummy.next = head
        while p.next:
            if p.next.val == val:
                p.next = p.next.next
                break
            p = p.next
        return dummy.next
