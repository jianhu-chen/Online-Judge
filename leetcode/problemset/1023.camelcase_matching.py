#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# https://leetcode.cn/problems/camelcase-matching
import re
from typing import List


class Solution:
    def camelMatch(self, queries: List[str], pattern: str) -> List[bool]:
        pc = re.findall(r"[A-Z][a-z]*", pattern)
        qc = map(lambda x: re.findall(r"[A-Z][a-z]*", x), queries)
        res = []
        for idx, q in enumerate(qc):
            if len(q) != len(pc):
                res.append(False)
                continue
            for pi, qi in zip(pc, q):
                i, j = 0, 0
                while i < len(pi) and j < len(qi):
                    if pi[i] == qi[j]:
                        i += 1
                        j += 1
                    else:
                        j += 1
                if i != len(pi):
                    res.append(False)
                    break
            if len(res) != idx + 1:
                res.append(True)
        return res
