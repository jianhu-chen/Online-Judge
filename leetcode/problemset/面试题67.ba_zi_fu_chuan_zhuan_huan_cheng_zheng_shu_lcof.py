#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# https://leetcode.cn/problems/ba-zi-fu-chuan-zhuan-huan-cheng-zheng-shu-lcof
import re


class Solution:
    def strToInt(self, s: str) -> int:
        return max(min(int(*re.findall("^[\+\-]?\d+", s.lstrip())), 2**31 - 1), -2**31)
