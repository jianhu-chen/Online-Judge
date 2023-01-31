#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# https://leetcode.cn/problems/longest-substring-without-repeating-characters
from collections import Counter


class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        cnt = Counter()
        left = 0
        ans = 0
        for right, x in enumerate(s):
            cnt[x] += 1
            while cnt[x] > 1:
                cnt[s[left]] -= 1
                left += 1
            ans = max(ans, right - left + 1)
        return ans
