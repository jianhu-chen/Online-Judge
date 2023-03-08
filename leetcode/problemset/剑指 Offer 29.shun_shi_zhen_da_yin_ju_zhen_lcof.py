#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# https://leetcode.cn/problems/shun-shi-zhen-da-yin-ju-zhen-lcof
from typing import List


class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        if not matrix:
            return []
        ans = []
        m, n = len(matrix), len(matrix[0])
        tt, bb, ll, rr = 0, m - 1, 0, n - 1
        while tt <= bb and ll <= rr:
            for jj in range(ll, rr + 1):  # 左到右
                ans.append(matrix[tt][jj])
            for ii in range(tt + 1, bb + 1):  # 上到下
                ans.append(matrix[ii][rr])
            if tt == bb: break  # 特判: 奇数行
            for jj in range(rr - 1, ll, -1):  # 右到左
                ans.append(matrix[bb][jj])
            if ll == rr: break  # 特判: 奇数列
            for ii in range(bb, tt, -1):  # 下到上
                ans.append(matrix[ii][ll])
            tt, bb, ll, rr = tt + 1, bb - 1, ll + 1, rr - 1
        return ans
