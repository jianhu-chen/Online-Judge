#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# https://leetcode.cn/problems/decrease-elements-to-make-array-zigzag
from typing import List


class Solution:
    def movesToMakeZigzag(self, nums: List[int]) -> int:
        n = len(nums)
        ans = [0, 0]
        for i, x in enumerate(nums):
            left = nums[i - 1] if i != 0 else float("inf")
            right = nums[i + 1] if i != n - 1 else float("inf")
            # ans[0]: /\/\  ans[1]: \/\/
            ans[i & 1] += max(0, x - min(left, right) + 1)
        return min(ans)
