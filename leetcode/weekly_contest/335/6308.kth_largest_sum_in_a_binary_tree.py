#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# https://leetcode.cn/problems/kth-largest-sum-in-a-binary-tree
from heapq import heapify, heappop
from random import randint
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def kthLargestLevelSum(self, root: Optional[TreeNode], k: int) -> int:
        nodes, ss = [root], []
        while nodes:
            tmp, s = [], 0
            for node in nodes:
                s -= node.val
                if node.left:
                    tmp.append(node.left)
                if node.right:
                    tmp.append(node.right)
            ss.append(s)
            nodes = tmp

        if len(ss) < k:
            return -1

        # 也可以用快速选择找第k大的数
        heapify(ss)
        while k - 1:
            heappop(ss)
            k -= 1
        return -ss[0]

    def solution2(self, root: Optional[TreeNode], k: int) -> int:
        """快速选择."""
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

        if len(ss) < k:
            return -1

        def quick_select(nums, L, R, kk):
            if L >= R:
                return
            left, idx, right = L - 1, L, R
            pivot_idx = randint(L, R)
            nums[pivot_idx], nums[R] = nums[R], nums[pivot_idx]
            while idx < right:
                if nums[idx] > nums[R]:
                    left += 1
                    nums[left], nums[idx] = nums[idx], nums[left]
                    idx += 1
                elif nums[idx] < nums[R]:
                    right -= 1
                    nums[right], nums[idx] = nums[idx], nums[right]
                else:
                    idx += 1
            nums[right], nums[R] = nums[R], nums[right]
            if kk > left and kk <= right:
                return
            elif kk > right:
                quick_select(nums, right + 1, R, kk)
            elif kk <= left:
                quick_select(nums, L, left, kk)

        quick_select(ss, 0, len(ss) - 1, k - 1)
        return ss[k - 1]
