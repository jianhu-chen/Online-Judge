#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# https://leetcode.cn/problems/minimum-operations-to-make-array-equal-ii
from typing import List


class Solution:
    def minOperations(self, nums1: List[int], nums2: List[int], k: int) -> int:
        # [4, 3, 1, 4] - [1, 3, 7, 1]
        # diff: [3, 0, -6, 3]
        # 和必须为0且每个差值元素能整除k
        # [3, 8, 5, 2] - [2, 4, 1, 6]
        # [1, 4, 4, -4]  # 失败
        diff = [n1 - n2 for n1, n2 in zip(nums1, nums2)]
        if k == 0:
            return 0 if nums1 == nums2 else -1

        ans = 0
        ps, ns = 0, 0
        for d in diff:
            if d > 0:
                ps += d
                ans += (d // k)
            else:
                ns += d
            if d % k != 0:
                return -1

        if ps != -ns:
            return -1
        else:
            return ans
