## 题目描述
# 大家都知道斐波那契数列，现在要求输入一个整数n，请你输出斐波那契数列的第n项（从0开始，第0项为0）。
# n<=39

# -*- coding:utf-8 -*-
# # 方法一：循环
# # 运行时间：25ms
# # 占用内存：5868k
# class Solution:
#     def Fibonacci(self, n):
#         # write code here
#         fir = 1
#         sec = 1
#         if n == 0:
#             return 0
#         elif n == 1 or n == 2:
#             return 1
#         else:
#             for _ in range(3, n+1):
#                 s = fir + sec
#                 fir = sec
#                 sec = s
#             return s


# # 方法二：递归
# # 判题编译器说时间复杂度太大 😺
# class Solution:
#     def Fibonacci(self, n):
#         # write code here
#         fir = 1
#         sec = 1
#         if n == 0:
#             return 0
#         elif n == 1 or n == 2:
#             return 1
#         else:
#             return self.Fibonacci(n-1) + self.Fibonacci(n-2)


# 方法三：动态规划 时间复杂度O(n)
# 运行时间：26ms 😃 哈哈，时间还长一些，很迷。。。
# 占用内存：5856k
class Solution:
    def Fibonacci(self, n):
        # write code here
        # write code here
        if n == 0:
            return 0
        dict_ = dict()
        dict_[1] = 1
        dict_[2] = 1
        for i in range(3, n+1):
            dict_[i] = dict_[i-1] + dict_[i-2]
        return dict_[n]


# 动态规划变型：记忆法
# 运行时间：36ms
# 占用内存：5752k
# class Solution:
#     def __init__(self):
#         self.mem_table = {1: 1, 2: 1}

#     def Fibonacci(self, n):
#         # write code here
#         if n == 0:
#             return 0

#         try:
#             return self.mem_table[n]
#         except:
#             pass

#         try:
#             f_n_1 = self.mem_table[n-1]
#         except:
#             f_n_1 = self.Fibonacci(n-1)
#             self.mem_table[n-1] = f_n_1

#         try:
#             f_n_2 = self.mem_table[n-2]
#         except:
#             f_n_2 = self.Fibonacci(n-2)
#             self.mem_table[n-2] = f_n_2

#         return f_n_1 + f_n_2


if __name__ == "__main__":
    n = 1
    S = Solution()
    rst = S.Fibonacci(n)
    print(rst)