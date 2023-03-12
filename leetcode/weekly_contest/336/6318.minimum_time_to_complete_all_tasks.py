#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# https://leetcode.cn/problems/minimum-time-to-complete-all-tasks
from typing import List


class Solution:
    def findMinimumTime(self, tasks: List[List[int]]) -> int:
        tasks.sort(key=lambda x: x[1])
        times = set()

        for start, end, duration in tasks:
            # 先复用
            reused = set()
            for t in range(start, end + 1):
                if t in times:
                    duration -= 1
                    reused.add(t)
                if duration == 0:
                    break

            # 贪心: 从右到左
            t = end
            while duration:
                if t not in reused:
                    times.add(t)
                    duration -= 1
                t -= 1

        return len(times)
