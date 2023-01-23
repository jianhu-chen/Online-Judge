#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# https://leetcode.cn/problems/maximize-the-minimum-powered-city
from typing import List
from itertools import accumulate


class Solution:
    def maxPower(self, stations: List[int], r: int, k: int) -> int:
        """二分 + 前缀和 + 差分."""
        n = len(stations)
        sum = list(accumulate(stations, initial=0))  # 前缀和
        for i in range(n):
            stations[i] = sum[min(i + r + 1, n)] - sum[max(i - r, 0)]  # 电量

        def check(min_power: int) -> bool:
            diff = [0] * n  # 差分数组
            sum_d = need = 0
            for i, power in enumerate(stations):
                sum_d += diff[i]  # 累加差分值
                m = min_power - power - sum_d
                if m > 0:  # 需要 m 个供电站
                    need += m
                    if need > k:
                        return False  # 提前退出这样快一些
                    sum_d += m  # 差分更新
                    if i + r * 2 + 1 < n:
                        diff[i + r * 2 + 1] -= m  # 差分更新
            return True

        left = min(stations)
        right = left + k + 1  # 开区间写法
        while left + 1 < right:
            mid = (left + right) // 2
            if check(mid):
                left = mid
            else:
                right = mid
        return left
