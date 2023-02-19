#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# https://leetcode.cn/problems/lian-biao-zhong-dao-shu-di-kge-jie-dian-lcof

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def getKthFromEnd(self, head: ListNode, k: int) -> ListNode:
        fast = slow = head
        while k > 1:
            fast = fast.next
            k -= 1
        while fast.next:
            slow = slow.next
            fast = fast.next
        return slow
