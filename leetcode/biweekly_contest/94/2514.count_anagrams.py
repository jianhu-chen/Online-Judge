#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# https://leetcode.cn/problems/count-anagrams
from collections import Counter


class Solution:
    def countAnagrams(self, s: str) -> int:
        ans = 1
        for word in s.split(" "):
            # 长度为n的字符串 too
            # 全排列(且去重): n! / x!
            cnt = Counter()
            a = 1
            for i, ch in enumerate(word, 1):
                a *= i
                cnt[ch] += 1
                a //= cnt[ch]
            ans *= a
        return ans % (10 ** 9 + 7)
