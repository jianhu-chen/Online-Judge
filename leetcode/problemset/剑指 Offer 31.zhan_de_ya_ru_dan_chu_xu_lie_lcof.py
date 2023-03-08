#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# https://leetcode.cn/problems/zhan-de-ya-ru-dan-chu-xu-lie-lcof
from typing import List


class Solution:
    def validateStackSequences(self, pushed: List[int], popped: List[int]) -> bool:
        stack, j = [], 0
        for x in pushed:
            stack.append(x)
            while stack and stack[-1] == popped[j]:
                stack.pop()
                j += 1
        return len(stack) == 0
