#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# https://leetcode.cn/problems/power-of-two

class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        return (n & (n - 1)) == 0 and n != 0
