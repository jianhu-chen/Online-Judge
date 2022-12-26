#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# https://leetcode.cn/problems/longest-palindromic-substring

class Solution:
    def longestPalindrome(self, s: str) -> str:
        # manacher
        s = "#" + "#".join(list(s)) + "#"

        max_r = 0
        max_str = ""
        R = -1
        C = -1
        arr = [1 for _ in s]
        for i in range(len(s)):
            # 至少不用验证的回文半径
            offset = min(arr[2 * C - i], R - i) if i < R else 1

            while i - offset >= 0 and i + offset < len(s):
                if s[i - offset] != s[i + offset]:
                    break
                offset += 1

            arr[i] = offset
            if i + offset > R:
                C = i
                R = i + offset

            if offset > max_r:
                max_r = offset
                max_str = s[i - offset + 1: i + offset]

        return max_str[1::2]
