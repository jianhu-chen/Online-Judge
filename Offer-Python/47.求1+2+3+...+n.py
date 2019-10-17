## 题目描述
# 求1+2+3+...+n，要求不能使用乘除法、for、while、if、else、switch、case等关键字及条件判断语句（A?B:C）。


# -*- coding:utf-8 -*-
class Solution:
    def __init__(self):
        self.sum = 0

    def get_sum(self, n):
        self.sum += n
        # 利用逻辑短路机制终止递归
        return n>0 and self.get_sum(n-1)
        
    def Sum_Solution(self, n):
        # write code here
        # return sum(range(1, n+1))
        self.get_sum(n)
        return self.sum
        