#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# https://leetcode.cn/problems/next-greater-node-in-linked-list
from typing import List, Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def nextLargerNodes(self, head: Optional[ListNode]) -> List[int]:
        nums = []
        while head:
            nums.append(head.val)
            head = head.next

        # 单调递减栈
        stack = []
        right = [0] * len(nums)
        for i in range(len(nums) - 1, -1, -1):
            while stack and nums[i] >= nums[stack[-1]]:
                stack.pop()
            right[i] = nums[stack[-1]] if stack else 0
            stack.append(i)
        return right
