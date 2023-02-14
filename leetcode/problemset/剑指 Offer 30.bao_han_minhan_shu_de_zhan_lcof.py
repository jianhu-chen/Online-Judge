#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# https://leetcode.cn/problems/bao-han-minhan-shu-de-zhan-lcof

class MinStack:

    def __init__(self):
        """initialize your data structure here."""
        self.st = []
        self.mst = []

    def push(self, x: int) -> None:
        self.st.append(x)
        if not self.mst or x <= self.mst[-1]:
            self.mst.append(x)
        else:
            self.mst.append(self.mst[-1])

    def pop(self) -> None:
        self.st.pop()
        self.mst.pop()

    def top(self) -> int:
        return self.st[-1]

    def min(self) -> int:
        return self.mst[-1]


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(x)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.min()
