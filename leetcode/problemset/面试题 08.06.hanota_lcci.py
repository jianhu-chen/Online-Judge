#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# https://leetcode.cn/problems/hanota-lcci
from typing import List


class Solution:
    def hanota(self, A: List[int], B: List[int], C: List[int]) -> None:
        """Do not return anything, modify C in-place instead."""
        def move(n, F, T, oth):
            if n == 1:
                T.append(F.pop())
            else:
                move(n - 1, F, oth, T)
                T.append(F.pop())
                move(n - 1, oth, T, F)
        move(len(A), A, C, B)
