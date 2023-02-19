#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# https://leetcode.cn/problems/diao-zheng-shu-zu-shun-xu-shi-qi-shu-wei-yu-ou-shu-qian-mian-lcof
from typing import List


class Solution:
    def exchange(self, nums: List[int]) -> List[int]:
        n, left = len(nums), -1
        for i in range(n):
            if nums[i] & 1:
                left += 1
                nums[left], nums[i] = nums[i], nums[left]
        return nums
