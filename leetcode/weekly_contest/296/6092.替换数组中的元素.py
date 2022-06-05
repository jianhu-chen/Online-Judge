# -*- coding: utf-8 -*-
from typing import List


class Solution:

    def arrayChange(self, nums: List[int], operations: List[List[int]]) -> List[int]:
        idx_map = {n: i for i, n in enumerate(nums)}
        for op in operations:
            nums[idx_map[op[0]]] = op[1]
            idx_map[op[1]] = idx_map[op[0]]
        return nums
