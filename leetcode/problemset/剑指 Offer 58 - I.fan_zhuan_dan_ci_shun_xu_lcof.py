#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# https://leetcode.cn/problems/fan-zhuan-dan-ci-shun-xu-lcof

class Solution:
    def reverseWords(self, s: str) -> str:
        return " ".join(s.split()[::-1])
