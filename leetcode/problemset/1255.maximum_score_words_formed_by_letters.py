#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# https://leetcode.cn/problems/maximum-score-words-formed-by-letters
from typing import List
from collections import Counter


class Solution:
    def maxScoreWords(self, words: List[str], letters: List[str], score: List[int]) -> int:
        rest, n = Counter(letters), len(words)
        # 每个单词的得分
        ws = {w: sum(score[ord(c) - ord('a')] for c in w) for w in words}
        s, ans = 0, 0

        def dfs(i):
            nonlocal s, ans
            if i == n:
                ans = max(ans, s)
                return
            # 不选
            dfs(i + 1)
            # 选 (首先判断可以选)
            if all(rest[ch] >= cnt for ch, cnt in Counter(words[i]).items()):
                for ch, cnt in Counter(words[i]).items():
                    rest[ch] -= cnt
                s += ws[words[i]]
                dfs(i + 1)
                for ch, cnt in Counter(words[i]).items():
                    rest[ch] += cnt
                s -= ws[words[i]]

        dfs(0)
        return ans
