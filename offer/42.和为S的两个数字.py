## 题目描述
# 输入一个递增排序的数组和一个数字S，在数组中查找两个数，
# 使得他们的和正好是S，如果有多对数字的和等于S，输出两个数的乘积最小的。

# 输出描述:
# > 对应每个测试案例，输出两个数，小的先输出。


# -*- coding:utf-8 -*-
class Solution:
    def FindNumbersWithSum(self, array, tsum):
        # write code here
        if not array:
            return []
        for a in array:
            try:
                j = array.index(tsum - a)
            except:
                pass
            else:
                b = array[j]
                return (a, b)
        return []


if __name__ == "__main__":
    array,tsum = [1,2,4,7,11,15],15
    s = Solution()
    result = s.FindNumbersWithSum(array, tsum)
    print(result)