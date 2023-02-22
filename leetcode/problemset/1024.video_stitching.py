#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# https://leetcode.cn/problems/video-stitching
from typing import List


class Solution:
    def videoStitching(self, clips: List[List[int]], time: int) -> int:
        mx = {}
        for s, e in clips:
            mx[s] = max(mx.get(s, 0), e)
        pre, end, ans = 0, 0, 0
        for i in range(time + 1):
            if i > end:
                return -1
            end = max(end, mx.get(i, 0))
            if i == pre and i != time:
                ans += 1
                pre = end
        return ans
