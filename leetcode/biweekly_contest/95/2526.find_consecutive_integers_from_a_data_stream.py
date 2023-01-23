#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# https://leetcode.cn/problems/find-consecutive-integers-from-a-data-stream

class DataStream:

    def __init__(self, value: int, k: int):
        self.v = value
        self.k = k
        self.cnt = 0

    def consec(self, num: int) -> bool:
        self.cnt = self.cnt + 1 if num == self.v else 0
        return self.cnt >= self.k


# Your DataStream object will be instantiated and called as such:
# obj = DataStream(value, k)
# param_1 = obj.consec(num)
