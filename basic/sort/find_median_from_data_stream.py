#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import random
import unittest
from statistics import median

from heap import Heap


class MedianFinder:
    """中位数是有序列表中间的数。如果列表长度是偶数，中位数则是中间两个数的平均值。

    例如，

    [2,3,4] 的中位数是 3

    [2,3] 的中位数是 (2 + 3) / 2 = 2.5

    设计一个支持以下两种操作的数据结构：

    void addNum(int num) - 从数据流中添加一个整数到数据结构中。
    double findMedian() - 返回目前所有元素的中位数。

    https://leetcode.cn/problems/find-median-from-data-stream/
    """

    def __init__(self):
        # 记录大于等于中位数的数
        self.min_heap = Heap(comparator=lambda x, y: x < y)
        # 记录小于中位数的数
        self.max_heap = Heap(comparator=lambda x, y: x > y)

    def addNum(self, num: int) -> None:
        if self.min_heap.empty() or num >= self.min_heap.top():
            self.min_heap.push(num)
            if self.min_heap.size() > self.max_heap.size() + 1:
                self.max_heap.push(self.min_heap.pop())
        else:
            self.max_heap.push(num)
            if self.max_heap.size() > self.min_heap.size():
                self.min_heap.push(self.max_heap.pop())

    def findMedian(self) -> float:
        if self.min_heap.size() > self.max_heap.size():
            return self.min_heap.top()
        else:
            return (self.min_heap.top() + self.max_heap.top()) / 2


class Tester(unittest.TestCase):

    def test_solution(self):
        obj = MedianFinder()
        max_stream_length = random.randint(20000, 30000)
        data = [random.randint(-10000, 10000) for _ in range(max_stream_length)]
        for idx, num in enumerate(data, 1):
            obj.addNum(num)
            if random.random() > 0.9:
                self.assertEqual(obj.findMedian(), median(data[:idx]), data[:idx])


if __name__ == "__main__":
    unittest.main()
