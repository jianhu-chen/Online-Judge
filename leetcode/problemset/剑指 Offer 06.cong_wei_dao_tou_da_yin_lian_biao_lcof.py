#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# https://leetcode.cn/problems/cong-wei-dao-tou-da-yin-lian-biao-lcof
from typing import List


# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def reversePrint(self, head: ListNode) -> List[int]:
        ans = []
        while head:
            ans.append(head.val)
            head = head.next
        return ans[::-1]
