#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# https://leetcode.cn/problems/zui-chang-bu-han-zhong-fu-zi-fu-de-zi-zi-fu-chuan-lcof

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if not s:
            return 0
        ans, visited, left = 1, set(), 0
        for right, c in enumerate(s):
            while c in visited:
                visited.remove(s[left])
                left += 1
            visited.add(c)
            ans = max(ans, right - left + 1)
        return ans
