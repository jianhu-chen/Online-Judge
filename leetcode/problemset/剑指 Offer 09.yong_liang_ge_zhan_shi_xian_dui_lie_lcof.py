#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# https://leetcode.cn/problems/yong-liang-ge-zhan-shi-xian-dui-lie-lcof

class CQueue:

    def __init__(self):
        self.st1 = []
        self.st2 = []

    def appendTail(self, value: int) -> None:
        # 1 -> 2
        while self.st1:
            self.st2.append(self.st1.pop())
        self.st1.append(value)
        # 2 -> 1
        while self.st2:
            self.st1.append(self.st2.pop())

    def deleteHead(self) -> int:
        return -1 if not self.st1 else self.st1.pop()


# Your CQueue object will be instantiated and called as such:
# obj = CQueue()
# obj.appendTail(value)
# param_2 = obj.deleteHead()
