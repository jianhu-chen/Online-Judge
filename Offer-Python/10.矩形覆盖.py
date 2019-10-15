## 题目描述
# 我们可以用2*1的小矩形横着或者竖着去覆盖更大的矩形。
# 请问用n个2*1的小矩形无重叠地覆盖一个2*n的大矩形，总共有多少种方法？

# -*- coding:utf-8 -*-
class Solution:
    
    def __init__(self):
        self.table = {}

    def rectCover(self, number):
        # write code here
        # 方法1：递归，递归写法时间复杂度太高，不能通过
        # if number == 0:
        #     return 0
        # if number == 1:
        #     return 1
        # if number == 2:
        #     return 2
        # return self.rectCover(number-1) + self.rectCover(number-2)

        # 方法2：递归+记忆法，可以通过
        # if number == 0:
        #     return 0
        # if number == 1:
        #     return 1
        # if number == 2:
        #     return 2
        # if number-1 not in self.table.keys():
        #     self.table[number-1] = self.rectCover(number-1)
        # if number-2 not in self.table.keys():
        #     self.table[number-2] = self.rectCover(number-2)
        # return self.table[number-1] + self.table[number-2]

        # 方法3：循环推导法
        # if number == 0:
        #     return 0
        # if number == 1:
        #     return 1
        # if number == 2:
        #     return 2
        # i = 3
        # a = 1
        # b = 2
        # while i<=number:
        #     result = a + b
        #     a = b
        #     b = result
        #     i += 1
        # return result

        # 方法4：动态规划
        table = {0: 0, 1: 1, 2: 2}
        if number in table.keys():
            return table[number]

        for i in range(3, number+1):
            table[i] = table[i-1] + table[i-2]
        
        return table[number]


import time
if __name__ == "__main__":
    input = 100
    s = Solution()
    t0 = time.time()
    result = s.rectCover(input)
    print('result = {}, run time: {}'.format(result, time.time()-t0))
