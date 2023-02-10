#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from itertools import accumulate
from collections import defaultdict


class Solution:
    """https://codeforces.com/problemset/problem/1141/F2."""

    def sameSumBlocks(self, nums):
        # [4 1 2 2 1 5 3]
        ps = list(accumulate(nums, initial=0))
        n = len(nums)
        # 1. 暴力计算子集和到子集下标范围的映射(闭区间)
        s2ij = defaultdict(list)
        for lt in range(1, n + 1):
            for i in range(n - lt + 1):
                s = ps[i + lt] - ps[i]
                s2ij[s].append((i, i + lt - 1))

        # 2. 问题转换为: 求最多不重叠的线段个数(贪心, 右端点从小到大排列 + 遍历)
        ans = []
        for ijs in s2ij.values():
            pj = -1
            cans = []
            for i, j in sorted(ijs, key=lambda x: x[1]):
                if i > pj:
                    cans.append((i, j))
                    pj = j
            if len(cans) > len(ans):
                ans = cans
        return ans


if __name__ == "__main__":
    input()
    nums = [int(x) for x in input().strip().split()]
    # nums = [int(x) for x in "4 1 2 2 1 5 3".split()]
    # nums = [int(x) for x in "-5 -4 -3 -2 -1 0 1 2 3 4 5".split()]
    ans = Solution().sameSumBlocks(nums)
    print(len(ans))
    for i, j in ans:
        print(f"{i + 1} {j + 1}")
