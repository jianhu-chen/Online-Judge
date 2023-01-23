#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# https://leetcode.cn/problems/categorize-box-according-to-criteria

class Solution:
    def categorizeBox(self, length: int, width: int, height: int, mass: int) -> str:
        bulky, heavy = False, False
        if length * width * height >= 10 ** 9:
            bulky = True
        if not bulky:
            for item in (length, width, height, mass):
                if item >= 10 ** 4:
                    bulky = True
                    break

        if mass >= 100:
            heavy = True

        if bulky and heavy:
            return "Both"
        elif not bulky and not heavy:
            return "Neither"
        elif bulky:
            return "Bulky"
        else:
            return "Heavy"
