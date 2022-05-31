## 题目描述
# 输入一个整数数组，实现一个函数来调整该数组中数字的顺序，使得所有的奇数位于数组的前半部分，
# 所有的偶数位于数组的后半部分，并保证奇数和奇数，偶数和偶数之间的相对位置不变。

# 解法1：用两个数组，最后拼接
# 运行时间：27ms
# 占用内存：5948k
# -*- coding:utf-8 -*-
# class Solution:
#     def reOrderArray(self, array):
#         # write code here
#         arr1 = []
#         arr2 = []
#         for i in array:
#             if i%2 == 0:
#                 arr2.append(i)
#             else:
#                 arr1.append(i)
#         return arr1+arr2


# 方法2：
# 运行时间：30ms
# 占用内存：5752k
# -*- coding:utf-8 -*-
class Solution:
    def reOrderArray(self, array):
        # write code here
        pos = 0
        res = []
        for n in array:
            if n % 2 != 0:
                res.insert(pos, n)
                pos += 1
            else:
                res.append(n)
        return res
