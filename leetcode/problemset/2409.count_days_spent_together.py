#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# https://leetcode.cn/problems/count-days-spent-together

class Solution:
    def countDaysTogether(self, arriveAlice: str, leaveAlice: str, arriveBob: str, leaveBob: str) -> int:
        days = (31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31)
        start, end = max(arriveAlice, arriveBob), min(leaveAlice, leaveBob)
        if end < start:
            return 0
        (m1, d1), (m2, d2) = map(int, start.split("-")), map(int, end.split("-"))
        cnt = sum(days[m] for m in range(m1 - 1, m2))
        if m1 == m2:
            return d2 - d1 + 1
        cnt -= d1 - 1
        cnt -= days[m2 - 1] - d2
        return cnt
