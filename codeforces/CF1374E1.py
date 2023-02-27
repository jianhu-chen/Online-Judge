#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import heapq
from typing import List


class Solution:
    """https://codeforces.com/contest/1374/problem/E1.

    思路:
    1. 对书分类讨论:
        a. AB都喜欢
        b. A喜欢, B不喜欢
        c. A不喜欢, B喜欢
        d. AB都不喜欢
    显然, 第4类书不是我们需要的, 直接忽略即可.
    2. (贪心策略) 构造3个堆(h1, h2, h3)分别存放前3类书, 每次选书时:
        比较h1的堆顶元素与h2+h3的堆顶元素, 选择较小的，然后将k - 1
        循环往复, 直到满足AB都至少有k本书这个条件, 或者无书可选时直接返回-1.
    """

    def readingBooks(self, k: int, books: List[List[int]]) -> int:
        h1, h2, h3 = [], [], []
        for t, a, b in books:
            if not a and not b:
                continue
            if a and b:
                heapq.heappush(h1, t)
            elif a:
                heapq.heappush(h2, t)
            else:
                heapq.heappush(h3, t)
        ans = 0
        while k:
            if h1 and h2 and h3:
                if h1[0] <= h2[0] + h3[0]:
                    ans += heapq.heappop(h1)
                else:
                    ans += heapq.heappop(h2) + heapq.heappop(h3)
            elif h1:
                ans += heapq.heappop(h1)
            elif h2 and h3:
                ans += heapq.heappop(h2) + heapq.heappop(h3)
            else:
                return -1
            k -= 1
        return ans


if __name__ == "__main__":
    n, k = map(int, input().split())
    books = []
    for _ in range(n):
        t, a, b = map(int, input().split())
        books.append([t, a, b])
    print(Solution().readingBooks(k, books))
