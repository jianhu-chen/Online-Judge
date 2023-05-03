#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# https://leetcode.cn/problems/check-if-word-is-valid-after-substitutions
import re


class Solution:
    def isValid(self, s: str) -> bool:
        return self.solution2(s)

    def solution1(self, s: str) -> bool:
        """正则."""
        while s:
            new_s = re.sub(r"abc", "", s)
            if new_s == s:
                return False
            s = new_s
        return True

    def solution2(self, s: str) -> bool:
        """栈."""
        st = []
        for i, ch in enumerate(s):
            if ch == 'c' and len(st) >= 2 and st[-1] == 'b' and st[-2] == 'a':
                st.pop()
                st.pop()
            else:
                st.append(ch)
        return len(st) == 0
