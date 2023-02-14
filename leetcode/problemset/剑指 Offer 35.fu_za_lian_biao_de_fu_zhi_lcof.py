#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# https://leetcode.cn/problems/fu-za-lian-biao-de-fu-zhi-lcof

# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random


class Solution:
    def copyRandomList(self, head: 'Node') -> 'Node':
        if not head:
            return

        # 复制节点
        dummy = head
        while dummy:
            nxt = dummy.next
            dummy.next = Node(dummy.val, nxt)
            dummy = dummy.next.next

        # 复制 random 指针
        dummy = head
        while dummy:
            if dummy.random:
                dummy.next.random = dummy.random.next
            dummy = dummy.next.next

        # 分离
        dummy = head
        new_dummy = new = dummy.next
        while dummy:
            dummy.next = dummy.next.next
            dummy = dummy.next
            new.next = dummy.next if dummy else None
            new = new.next

        return new_dummy
