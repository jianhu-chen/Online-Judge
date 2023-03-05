#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# https://leetcode.cn/problems/split-the-array-to-make-coprime-products
from typing import List


class Solution:
    def findValidSplit(self, nums: List[int]) -> int:
        """本质是想找使得左右两边没有相同质因子的最小index."""
        # 4 7 8 15 3 5
        # 2 7 2 | 3 5
        # 不能把两个质因子放在两侧 => 哪些地方不能分割?
        left = {}  # left[p] 表示第一个以 p 为质因子的数的下标
        right = [-1] * len(nums)  # right[i] 表示左端点为 i 的区间的右端点的最大值

        def f(p, i):
            if p not in left:  # 质因子 p 第一次出现
                left[p] = i
            else:
                right[left[p]] = i

        for i, n in enumerate(nums):
            d = 2
            while d * d <= n:
                if n % d == 0:
                    f(d, i)
                    while n % d == 0:
                        n //= d
                d += 1
            if n > 1:
                f(n, i)

        # 参考 55. 跳跃游戏
        max_r = 0
        for ll, rr in enumerate(right):
            if ll > max_r:
                return max_r
            max_r = max(max_r, rr)
        return -1
