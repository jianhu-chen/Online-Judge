#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# https://leetcode.cn/problems/masking-personal-information
import re


class Solution:
    def maskPII(self, s: str) -> str:
        if '@' in s:
            s = s.lower()
            s1, s2 = s.split('@')
            return f"{s1[0]}*****{s1[-1]}@{s2}"
        else:
            s = re.sub(r"\+|\-|\(|\)|\s", '', s)
            return (f"+{'*' * (len(s) - 10)}-" if len(s) > 10 else "") + f"***-***-{s[-4:]}"
