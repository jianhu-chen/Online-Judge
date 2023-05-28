#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# https://leetcode.cn/problems/remove-trailing-zeros-from-a-string

class Solution:
    def removeTrailingZeros(self, num: str) -> str:
        return num.rstrip('0')