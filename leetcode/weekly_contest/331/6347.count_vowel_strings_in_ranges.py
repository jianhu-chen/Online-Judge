#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# https://leetcode.cn/problems/count-vowel-strings-in-ranges
from typing import List
from itertools import accumulate


class Solution:
    def vowelStrings(self, words: List[str], queries: List[List[int]]) -> List[int]:
        ps = list(accumulate(
            (1 if w[0] in "aeiou" and w[-1] in "aeiou" else 0 for w in words),
            initial=0
        ))
        return [ps[j + 1] - ps[i] for i, j in queries]
