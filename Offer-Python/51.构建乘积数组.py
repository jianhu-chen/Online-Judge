## 题目描述
# 给定一个数组A[0,1,...,n-1],请构建一个数组B[0,1,...,n-1],
# 其中B中的元素B[i]=A[0]*A[1]*...*A[i-1]*A[i+1]*...*A[n-1]。
# 
# Note: 不能使用除法。


# -*- coding:utf-8 -*-
import copy
class Solution:
    def multiply(self, A):
        # write code here
        B = [1 for i in range(len(A))]
        for i in range(len(A)):
            T = copy.deepcopy(A)
            T.pop(i)
            for j in range(len(T)):
                B[i] = B[i]*T[j]
        return B
