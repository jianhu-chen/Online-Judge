#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# https://leetcode.cn/problems/pass-the-pillow

class Solution:
    def passThePillow(self, n: int, time: int) -> int:
        t, r = time // (n - 1), time % (n - 1)
        return n - r if t & 1 else r + 1
