## 题目描述
# 一只青蛙一次可以跳上1级台阶，也可以跳上2级……它也可以跳上n级。
# 求该青蛙跳上一个n级的台阶总共有多少种跳法。


# -*- coding:utf-8 -*-
class Solution:
    def jumpFloorII(self, number):
        # write code here
        fir = 1
        sec = 2
        if number == 1:
            return 1
        elif number == 2:
            return 2
        else:
            res = 0
            for i in range(1, number):
                res += self.jumpFloorII(i)
            return res+1 # +1是因为可以从0阶跳起

# 可以使用动态规划方法解此题
# 使用动态规划的变型：记忆法：
# 用一个字典记录每一个jumpFloorII(i)的值，这样就避免了很多重复计算
# class Solution:
#     def __init__(self):
#         self.table = {}

#     def jumpFloorII(self, number):
#         # write code here
#         fir = 1
#         sec = 2
#         if number == 1:
#             return 1
#         elif number == 2:
#             return 2
#         else:
#             res = 0
#             for i in range(1, number):
#                 if i in self.table.keys():
#                     res += self.table[i]
#                 else:
#                     self.table[i] = self.jumpFloorII(i)
#                     res += self.table[i]
#             return res+1 # +1是因为可以从0阶跳起
