#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# https://leetcode.cn/problems/surrounded-regions
from typing import List


class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """Do not return anything, modify board in-place instead."""
        M, N = len(board), len(board[0])

        def infect(x, y):
            if x < 0 or x >= M or y < 0 or y >= N or board[x][y] != "O":
                return
            board[x][y] = "o"
            infect(x - 1, y)
            infect(x + 1, y)
            infect(x, y - 1)
            infect(x, y + 1)

        for y in range(N):
            infect(0, y)
            infect(M - 1, y)

        for x in range(M):
            infect(x, 0)
            infect(x, N - 1)

        for x in range(M):
            for y in range(N):
                if board[x][y] == "O":
                    board[x][y] = "X"
                elif board[x][y] == "o":
                    board[x][y] = "O"
