#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# https://leetcode.cn/problems/sort-the-students-by-their-kth-score
from typing import List


class Solution:
    def sortTheStudents(self, score: List[List[int]], k: int) -> List[List[int]]:
        score.sort(key=lambda x: -x[k])
        return score
