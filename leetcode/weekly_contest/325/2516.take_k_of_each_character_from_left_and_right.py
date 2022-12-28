#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# https://leetcode.cn/problems/take-k-of-each-character-from-left-and-right

class Solution:
    def takeCharacters(self, s: str, k: int) -> int:
        # 前缀为空:
        # aabaaaacaabc
        #   baaaacaabc
        # 开始加前缀
        # a baaaacaabc
        # aa baaaacaabc
        # aab caabc
        n = len(s)
        j = n
        counter = [0, 0, 0]
        while counter[0] < k or counter[1] < k or counter[2] < k:
            if j == 0:
                return -1
            j -= 1
            counter[ord(s[j]) - ord('a')] += 1

        ans = n - j
        i = 0
        while i < n and j < n:
            counter[ord(s[i]) - ord('a')] += 1
            while j < n and counter[ord(s[j]) - ord('a')] > k:
                counter[ord(s[j]) - ord('a')] -= 1
                j += 1
            ans = min(ans, i + 1 + n - j)
            i += 1
        return ans
