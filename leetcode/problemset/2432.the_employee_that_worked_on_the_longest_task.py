#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# https://leetcode.cn/problems/the-employee-that-worked-on-the-longest-task
from typing import List


class Solution:
    def hardestWorker(self, n: int, logs: List[List[int]]) -> int:
        prev_leave, max_time, max_idx = 0, 0, 0
        for idx, leave_time in logs:
            diff = leave_time - prev_leave
            if diff > max_time or (diff == max_time and idx < max_idx):
                max_time = diff
                max_idx = idx
            prev_leave = leave_time
        return max_idx
