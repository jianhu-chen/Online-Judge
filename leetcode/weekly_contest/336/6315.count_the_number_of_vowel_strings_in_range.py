#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# https://leetcode.cn/problems/count-the-number-of-vowel-strings-in-range
from typing import List


class Solution:
    def vowelStrings(self, words: List[str], left: int, right: int) -> int:
        return sum(w[0] in "aeiou" and w[-1] in "aeiou" for w in words[left:right + 1])
