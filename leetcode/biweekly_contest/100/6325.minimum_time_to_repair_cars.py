#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# https://leetcode.cn/problems/minimum-time-to-repair-cars
from math import floor
from typing import List


class Solution:
    def repairCars(self, ranks: List[int], cars: int) -> int:

        def check(t):
            s = 0
            for r in ranks:
                s += floor((t / r) ** 0.5)
            return s >= cars

        L, R = 0, cars * cars * max(ranks)
        while L <= R:
            M = L + ((R - L) >> 1)
            if check(M):
                R = M - 1
            else:
                L = M + 1
        return R + 1
