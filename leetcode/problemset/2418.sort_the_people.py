#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# https://leetcode.cn/problems/sort-the-people
from typing import List


class Solution:
    def sortPeople(self, names: List[str], heights: List[int]) -> List[str]:
        return [x[0] for x in sorted(zip(names, heights), key=lambda x: -x[1])]
