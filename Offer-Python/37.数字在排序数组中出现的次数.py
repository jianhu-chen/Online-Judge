## 题目描述
# 统计一个数字在排序数组中出现的次数。


# -*- coding:utf-8 -*-
class Solution:
    def GetNumberOfK(self, data, k):
        # write code here
        l = list(data)
        return l.count(k)
