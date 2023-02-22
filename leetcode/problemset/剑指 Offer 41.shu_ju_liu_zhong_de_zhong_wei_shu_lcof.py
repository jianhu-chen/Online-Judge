#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# https://leetcode.cn/problems/shu-ju-liu-zhong-de-zhong-wei-shu-lcof
import heapq


class MedianFinder:

    def __init__(self):
        """initialize your data structure here."""
        self.mn = []
        self.mx = []

    def addNum(self, num: int) -> None:
        if not self.mn or num > self.mn[0]:
            heapq.heappush(self.mn, num)
            if len(self.mn) - len(self.mx) > 1:
                heapq.heappush(self.mx, -heapq.heappop(self.mn))
        else:
            heapq.heappush(self.mx, -num)
            if len(self.mx) - len(self.mn) > 0:
                heapq.heappush(self.mn, -heapq.heappop(self.mx))

    def findMedian(self) -> float:
        if len(self.mn) == len(self.mx):
            return (self.mn[0] - self.mx[0]) / 2
        return self.mn[0]


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()
