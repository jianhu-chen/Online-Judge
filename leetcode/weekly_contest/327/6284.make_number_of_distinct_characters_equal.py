#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# https://leetcode.cn/problems/make-number-of-distinct-characters-equal
from copy import deepcopy
from collections import Counter


class Solution:
    def isItPossible(self, word1: str, word2: str) -> bool:
        c1 = Counter(word1)
        c2 = Counter(word2)
        if len(c1) == len(c2):
            return True if set(c1.values()) & set(c2.values()) else False

        bigger = c1 if len(c1) >= len(c2) else c2
        smaller = c2 if bigger is c1 else c1

        for ch1 in list(bigger.keys()):
            for ch2 in list(smaller.keys()):
                bc = deepcopy(bigger)
                sc = deepcopy(smaller)
                bc[ch1] -= 1
                bc[ch2] += 1
                sc[ch1] += 1
                sc[ch2] -= 1
                if bc[ch1] == 0:
                    del bc[ch1]
                if sc[ch2] == 0:
                    del sc[ch2]
                if len(bc) == len(sc):
                    return True
        return False
