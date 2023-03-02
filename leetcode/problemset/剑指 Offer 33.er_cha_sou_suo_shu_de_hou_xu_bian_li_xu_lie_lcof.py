#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# https://leetcode.cn/problems/er-cha-sou-suo-shu-de-hou-xu-bian-li-xu-lie-lcof
from typing import List


class Solution:
    def verifyPostorder(self, postorder: List[int]) -> bool:

        def dfs(post, ll, rr):
            if not post:
                return True
            val = post[-1]
            if val > rr or val < ll:
                return False
            idx = len(post) - 2
            while idx >= 0 and post[idx] > val:
                idx -= 1
            return dfs(post[:idx + 1], ll, val) and dfs(post[idx + 1:len(post) - 1], val, rr)

        return dfs(postorder, -float("inf"), float("inf"))
