#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# https://leetcode.cn/problems/minimum-hours-of-training-to-win-a-competition
from typing import List


class Solution:
    def minNumberOfHours(self, initialEnergy: int, initialExperience: int, energy: List[int], experience: List[int]) -> int:
        ans = 0
        for eng, exp in zip(energy, experience):
            if eng < initialEnergy and exp < initialExperience:
                initialEnergy -= eng
                initialExperience += exp
            else:
                diff_eng, diff_exp = eng - initialEnergy, exp - initialExperience
                ans += diff_eng + 1 if diff_eng >= 0 else 0
                ans += diff_exp + 1 if diff_exp >= 0 else 0
                initialEnergy = 1 if diff_eng >= 0 else initialEnergy - eng
                initialExperience += diff_exp + 1 + exp if diff_exp >= 0 else exp
        return ans
