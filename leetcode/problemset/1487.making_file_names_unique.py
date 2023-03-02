#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# https://leetcode.cn/problems/making-file-names-unique
from typing import List
from collections import Counter


class Solution:
    def getFolderNames(self, names: List[str]) -> List[str]:
        cnt, ans = Counter(), []
        for n in names:
            if n in cnt:
                k = cnt[n]
                while n + f"({k})" in cnt:
                    k += 1
                cnt[n] = k + 1
                n += f"({k})"
            ans.append(n)
            cnt[n] += 1
        return ans
