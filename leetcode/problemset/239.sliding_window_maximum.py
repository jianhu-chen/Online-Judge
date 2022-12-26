#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# https://leetcode.cn/problems/sliding-window-maximum
from typing import List


class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        result = []
        deque = []
        for i in range(len(nums)):
            while deque and nums[deque[-1]] < nums[i]:
                deque.pop()
            deque.append(i)
            if deque[0] == i - k:
                deque.pop(0)
            if i >= k - 1:
                result.append(nums[deque[0]])
        return result
