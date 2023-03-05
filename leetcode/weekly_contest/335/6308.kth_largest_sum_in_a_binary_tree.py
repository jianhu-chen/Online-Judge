#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# https://leetcode.cn/problems/kth-largest-sum-in-a-binary-tree
from random import randint
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def quick_select(nums, L, R, k):
    """快速选择, 返回 nums 中第 k 大的数 (k 从 0 开始)."""
    t = randint(L, R)  # 随机partition
    nums[t], nums[R] = nums[R], nums[t]
    left, idx = L - 1, L
    while idx < R:
        if nums[idx] > nums[R]:
            left += 1
            nums[left], nums[idx] = nums[idx], nums[left]
        idx += 1
    left += 1
    nums[left], nums[R] = nums[R], nums[left]
    if left == k:
        return nums[left]
    elif left > k:
        return quick_select(nums, L, left - 1, k)
    elif left < k:
        return quick_select(nums, left + 1, R, k)


class Solution:
    def kthLargestLevelSum(self, root: Optional[TreeNode], k: int) -> int:
        nodes, ss = [root], []
        while nodes:
            tmp, s = [], 0
            for node in nodes:
                s += node.val
                if node.left:
                    tmp.append(node.left)
                if node.right:
                    tmp.append(node.right)
            ss.append(s)
            nodes = tmp

        return -1 if len(ss) < k else quick_select(ss, 0, len(ss) - 1, k - 1)
