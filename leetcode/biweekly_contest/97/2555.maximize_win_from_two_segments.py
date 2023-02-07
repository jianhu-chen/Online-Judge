#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# https://leetcode.cn/problems/maximize-win-from-two-segments
from typing import List


class Solution:
    def maximizeWin(self, prizePositions: List[int], k: int) -> int:
        """双指针."""
        ans = left = 0
        # pre[i] 表示到0...i-1，能获得的最多奖品数目
        pre = [0] * (len(prizePositions) + 1)
        for right, x in enumerate(prizePositions):
            while x - prizePositions[left] > k:
                left += 1
            ans = max(ans, right - left + 1 + pre[left])
            pre[right + 1] = max(pre[right], right - left + 1)
        return ans
