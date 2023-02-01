#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# https://leetcode.cn/problems/search-in-rotated-sorted-array
from typing import List


class Solution:
    def search(self, nums: List[int], target: int) -> int:
        pass

    def solution1(self, nums: List[int], target: int) -> int:
        # 1. 先确定搜索范围 O(logn)
        n = len(nums)
        if n == 1:
            return 0 if nums[0] == target else -1

        if nums[0] < nums[1] and nums[0] < nums[-1]:
            SL, SR = 0, n - 1  # 搜索范围左边界
        elif nums[-1] < nums[-2] and nums[-1] < nums[0]:
            if nums[-1] == target:
                return n - 1
            SL, SR = 0, n - 2
        else:
            # 先找到最小值
            L, R = 0, n - 1
            while L <= R:
                M = L + ((R - L) >> 1)
                if nums[M] < nums[M - 1] and nums[M] < nums[M + 1]:
                    if target >= nums[0]:
                        SL, SR = 0, M - 1
                    else:
                        SL, SR = M, n - 1
                    break
                elif nums[M] >= nums[0]:
                    L = M + 1
                elif nums[M] <= nums[-1]:
                    R = M - 1

        # 2. 在二分查找 O(logn)
        L, R = SL, SR
        while L <= R:
            M = L + ((R - L) >> 1)
            if nums[M] < target:
                L += 1
            elif nums[M] > target:
                R -= 1
            else:
                return M

        return -1

    def solution2(self, nums: List[int], target: int) -> int:
        """简洁版: 分类讨论."""
        n = len(nums)
        if n == 1:
            return 0 if nums[0] == target else -1
        L, R = 0, n - 1
        while L <= R:
            M = L + ((R - L) >> 1)
            if nums[M] > target:
                if nums[M] > nums[-1] and target <= nums[-1]:
                    L = M + 1
                else:
                    R = M - 1
            elif nums[M] < target:
                if nums[M] < nums[0] and target >= nums[0]:
                    R = M - 1
                else:
                    L = M + 1
            else:
                return M
        return -1
