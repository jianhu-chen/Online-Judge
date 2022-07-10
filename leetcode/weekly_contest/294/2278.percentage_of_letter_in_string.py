#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# https://leetcode.cn/problems/percentage-of-letter-in-string

class Solution:
    def percentageLetter(self, s: str, letter: str) -> int:
        return s.count(letter) * 100 // len(s)
