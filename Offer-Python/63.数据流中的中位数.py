## 题目描述
# 如何得到一个数据流中的中位数？
# 如果从数据流中读出奇数个数值，那么中位数就是所有数值排序之后位于中间的数值。
# 如果从数据流中读出偶数个数值，那么中位数就是所有数值排序之后中间两个数的平均值。
# 我们使用Insert()方法读取数据流，使用GetMedian()方法获取当前读取数据的中位数。

# -*- coding:utf-8 -*-
class Solution:
    def __init__(self):
        self.values = []

    def Insert(self, num):
        # write code here
        self.values.append(num)

    def GetMedian(self):
        # write code here
        self.values.sort()
        l = len(self.values)
        if l % 2 == 0:
            return (self.values[int(l/2) - 1] + self.values[int(l/2)]) / 2.0
        else:
            return self.values[int(l/2)]