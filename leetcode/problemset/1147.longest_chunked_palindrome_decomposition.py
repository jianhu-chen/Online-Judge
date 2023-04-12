#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# https://leetcode.cn/problems/longest-chunked-palindrome-decomposition

class Solution:
    def longestDecomposition(self, text: str) -> int:
        """贪心."""
        if not text:
            return 0
        for i in range(1, len(text)):
            if text[:i] == text[-i:]:
                return 2 + self.longestDecomposition(text[i:-i])
        return 1
