#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# https://leetcode.cn/problems/minimum-additions-to-make-valid-string
import re


class Solution:
    def addMinimum(self, word: str) -> int:
        f = re.findall(r"abc|ab|bc|ac|a|b|c", word)
        return sum(3 - len(x) for x in f)
