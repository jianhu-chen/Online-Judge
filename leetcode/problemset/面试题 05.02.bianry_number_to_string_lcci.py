#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# https://leetcode.cn/problems/bianry-number-to-string-lcci

class Solution:
    def printBin(self, num: float) -> str:
        # 在二进制表示中，将一个数乘以 2 的效果是将小数点向右移动一位
        ans = "0."
        while num and len(ans) <= 32:
            num *= 2
            if num >= 1:
                ans += "1"
                num -= 1
            else:
                ans += "0"
        return ans if len(ans) <= 32 else "ERROR"
