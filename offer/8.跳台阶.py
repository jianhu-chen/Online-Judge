## 题目描述
# 一只青蛙一次可以跳上1级台阶，也可以跳上2级。
# 求该青蛙跳上一个n级的台阶总共有多少种跳法
# （先后次序不同算不同的结果）。


# -*- coding:utf-8 -*-
# 与上一题斐波拉契数列同理，有4种解法
class Solution:
    def jumpFloor(self, number):
        # write code here
        fir = 1
        sec = 2
        if number == 1:
            return 1
        elif number == 2:
            return 2
        else:
            for i in range(3, number+1):
                s = fir + sec
                fir = sec
                sec = s
            return s
