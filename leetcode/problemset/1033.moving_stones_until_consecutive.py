#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# https://leetcode.cn/problems/moving-stones-until-consecutive
from typing import List


class Solution:
    def numMovesStones(self, a: int, b: int, c: int) -> List[int]:
        a, b, c = sorted((a, b, c))
        maximum_moves = c - a - 2

        minimum_moves = 2
        if c - b == b - a == 1:
            minimum_moves = 0
        elif c - b <= 2 or b - a <= 2:
            minimum_moves = 1
        return minimum_moves, maximum_moves
