#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# https://leetcode.cn/problems/longest-substring-without-repeating-characters


class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        """思路: 滑动窗口"""
        p2 = 0
        result = 0
        window = set()
        for p1 in range(len(s)):
            if p1 != 0:
                window.remove(s[p1 - 1])
            while p2 < len(s) and s[p2] not in window:
                window.add(s[p2])
                p2 += 1
            result = max(result, p2 - p1)
        return result


if __name__ == "__main__":
    print(Solution().lengthOfLongestSubstring(s="pwwkew"))
