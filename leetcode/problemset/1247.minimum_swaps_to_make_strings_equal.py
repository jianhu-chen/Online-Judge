#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# https://leetcode.cn/problems/minimum-swaps-to-make-strings-equal

class Solution:
    def minimumSwap(self, s1: str, s2: str) -> int:
        """贪心
        先统计相同位置不同字符的数量
        此时, 情况一: 不同字符的数量为奇数 => 不可能通过交换使两个字符串相同
             情况二: 不同字符的数量为偶数 => 细分两种两种情况:
                1: xy yx => 交换两次
                2: xx yy => 交换一次
        """
        xy, yx = 0, 0
        for c1, c2 in zip(s1, s2):
            if c1 == "x" and c2 == "y":
                xy += 1
            elif c1 == "y" and c2 == "x":
                yx += 1

        if (xy + yx) & 1:  # 如果不同位数位奇数, 直接返回-1
            return -1

        return (xy + yx) // 2 + (xy & 1)
