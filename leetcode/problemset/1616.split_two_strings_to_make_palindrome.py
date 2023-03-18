#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# https://leetcode.cn/problems/split-two-strings-to-make-palindrome

class Solution:
    def checkPalindromeFormation(self, a: str, b: str) -> bool:
        return self.solution2(a, b)

    def solution1(self, a: str, b: str) -> bool:
        """暴力解, O(n^2), 超时."""
        for i in range(len(a)):
            s1 = a[:i] + b[i:]
            if s1 == s1[::-1]:
                return True
            s2 = b[:i] + a[i:]
            if s2 == s2[::-1]:
                return True
        return False

    def solution2(self, a: str, b: str) -> bool:
        n = len(a)
        i = 0
        while i < n and (a[i] == b[n - 1 - i] or b[i] == a[n - 1 - i]):
            i += 1
        # 判断i有没有过中点
        if i >= n // 2:
            return True
        # 判断中间字串是否回文
        if b[i:n - i] == b[i:n - i][::-1] or a[i:n - i] == a[i:n - i][::-1]:
            return True
        return False
