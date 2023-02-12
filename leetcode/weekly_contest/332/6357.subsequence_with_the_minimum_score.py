#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# https://leetcode.cn/problems/subsequence-with-the-minimum-score

class Solution:
    def minimumScore(self, s: str, t: str) -> int:
        # 删除t中l...r的子串中的某些字符和删除整个字串的得分一样
        n, m = len(s), len(t)
        suffix = [m] * (n + 1)  # suffix[i] 表示i...m-1匹配到的后缀位置
        j = m - 1
        for i in reversed(range(n)):
            if j != -1 and s[i] == t[j]:
                j -= 1
            suffix[i] = j + 1
        print(suffix)

        ans = suffix[0]  # 0...m-1匹配到的t的后缀字符位置
        j = 0
        for i, c in enumerate(s):
            if j != m and c == t[j]:
                j += 1
                if suffix[i + 1] >= j:
                    ans = min(ans, suffix[i + 1] - j)
        return ans
