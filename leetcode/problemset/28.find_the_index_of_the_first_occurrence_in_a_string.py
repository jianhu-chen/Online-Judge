#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# https://leetcode.cn/problems/find-the-index-of-the-first-occurrence-in-a-string

class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        """KMP."""
        next_arr = [-1 for _ in needle]
        if len(needle) > 1:
            next_arr[1] = 0
            i = 2  # 当前在求哪个位置的数组值
            cn = 0  # 当前是哪个位置在与i-1位置的字符比较
            while i < len(needle):
                if needle[i - 1] == needle[cn]:
                    next_arr[i] = cn + 1
                    i += 1
                    cn += 1
                elif next_arr[cn] != -1:
                    cn = next_arr[cn]
                else:
                    next_arr[i] = 0
                    i += 1

        i, j = 0, 0
        while i < len(haystack) and j < len(needle):
            if haystack[i] == needle[j]:
                i += 1
                j += 1
            elif next_arr[j] != -1:
                j = next_arr[j]
            else:
                i += 1
        return i - j if j == len(needle) else -1
