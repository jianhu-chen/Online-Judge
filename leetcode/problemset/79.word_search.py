#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# https://leetcode.cn/problems/word-search
from typing import List


class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        m, n = len(board), len(board[0])

        def dfs(i, j, k):
            if k == len(word):
                return True
            if i == m or i == -1 or j == n or j == -1:
                return False
            if board[i][j] != word[k]:
                return False

            board[i][j] += " "
            ans = dfs(i, j - 1, k + 1) or dfs(i, j + 1, k + 1) or \
                dfs(i - 1, j, k + 1) or dfs(i + 1, j, k + 1)
            board[i][j] = board[i][j][0]
            return ans

        for i in range(m):
            for j in range(n):
                if dfs(i, j, 0):
                    return True

        return False
