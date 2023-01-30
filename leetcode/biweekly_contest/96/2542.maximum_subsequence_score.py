#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# https://leetcode.cn/problems/maximum-subsequence-score
import heapq
from typing import List


class Solution:
    def maxScore(self, nums1: List[int], nums2: List[int], k: int) -> int:
        # 组合nums1和nums2，再根据nums2降序排列，枚举k
        tmp = sorted(zip(nums1, nums2), key=lambda x: -x[1])
        heap = [x for x, _ in tmp[:k]]
        heapq.heapify(heap)
        s = sum(heap)
        ans = s * tmp[k - 1][1]
        for x, y in tmp[k:]:
            if x <= heap[0]:
                continue
            s += (x - heapq.heapreplace(heap, x))
            ans = max(ans, s * y)
        return ans
