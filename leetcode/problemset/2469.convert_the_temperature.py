#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# https://leetcode.cn/problems/convert-the-temperature
from typing import List


class Solution:
    def convertTemperature(self, celsius: float) -> List[float]:
        return celsius + 273.15, celsius * 1.8 + 32
