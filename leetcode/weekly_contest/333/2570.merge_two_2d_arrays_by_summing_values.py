#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# https://leetcode.cn/problems/merge-two-2d-arrays-by-summing-values
from typing import List


class Solution:
    def mergeArrays(self, nums1: List[List[int]], nums2: List[List[int]]) -> List[List[int]]:
        n1, n2 = len(nums1), len(nums2)
        p1, p2 = 0, 0
        ans = []
        while p1 < n1 and p2 < n2:
            i1, v1 = nums1[p1]
            i2, v2 = nums2[p2]
            if i1 < i2:
                ans.append(nums1[p1])
                p1 += 1
            elif i1 > i2:
                ans.append(nums2[p2])
                p2 += 1
            else:
                ans.append([i1, v1 + v2])
                p1 += 1
                p2 += 1

        if p1 < n1:
            ans.extend(nums1[p1:])

        if p2 < n2:
            ans.extend(nums2[p2:])

        return ans
