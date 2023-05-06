#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# https://leetcode.cn/problems/minimum-number-of-frogs-croaking

class Solution:
    def minNumberOfFrogs(self, croakOfFrogs: str) -> int:
        cnt = [0] * 5
        idx = dict(zip("croak", range(5)))
        pre = dict(zip("croak", "kcroa"))
        for ch in croakOfFrogs:
            pre_idx = idx[pre[ch]]
            if cnt[pre_idx]:
                cnt[pre_idx] -= 1  # 复用青蛙
            elif ch != 'c':
                return -1  # 必须从 c 开始叫
            cnt[idx[ch]] += 1
        if any(cnt[:4]):
            return -1
        return cnt[-1]
