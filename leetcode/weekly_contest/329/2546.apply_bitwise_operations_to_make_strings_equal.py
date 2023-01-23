#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# https://leetcode.cn/problems/apply-bitwise-operations-to-make-strings-equal

class Solution:
    def makeStringsEqual(self, s: str, target: str) -> bool:
        return ("1" in s) == ("1" in target)
