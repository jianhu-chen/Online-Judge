#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# https://leetcode.cn/problems/next-greater-element-i
from typing import List


class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        n = len(nums2)
        st, right = [], [-1] * len(nums2)
        for i in reversed(range(n)):
            while st and nums2[i] >= nums2[st[-1]]:
                st.pop()
            right[i] = st[-1] if st else -1
            st.append(i)
        m = dict(zip(nums2, range(n)))
        return [(nums2[right[m[x]]] if right[m[x]] != -1 else -1) for x in nums1]
