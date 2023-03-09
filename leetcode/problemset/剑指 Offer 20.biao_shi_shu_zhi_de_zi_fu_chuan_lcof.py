#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# https://leetcode.cn/problems/biao-shi-shu-zhi-de-zi-fu-chuan-lcof
import re


class Solution:
    def isNumber(self, s: str) -> bool:
        s = s.strip()
        return re.search(r"^[\+-]?\d+\.?\d*([eE][\+-]?\d+)?$|^[+-]?\.\d+([eE][\+-]?\d+)?$", s) is not None
