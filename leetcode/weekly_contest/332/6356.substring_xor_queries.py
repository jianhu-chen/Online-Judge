#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# https://leetcode.cn/problems/substring-xor-queries
from typing import List


class Solution:
    def substringXorQueries(self, s: str, queries: List[List[int]]) -> List[List[int]]:
        # val ^ first = second => first = second ^ first
        # 两个数异或的范围小于10 ** 9 => 小于 2^30 = 1073741824
        n = len(s)
        # 预处理, O(30n)
        m = {}  # {eor: (i, j)}
        for left in range(n):
            if s[left] == "0":
                if 0 not in m:
                    m[0] = (left, left)
                continue
            x = 0
            # +30取min是因为太长没有意义
            for right in range(left, min(left + 30, n)):
                x = (x << 1) | (ord(s[right]) - ord('0'))
                if x not in m:
                    m[x] = (left, right)
        NF = (-1, -1)
        # O(q)
        return [m.get(x ^ y, NF) for x, y in queries]
