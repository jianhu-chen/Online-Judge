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
        if number == 0:
            return 0
        if number == 1:
            return 1
        if number == 2:
            return 2
        i = 3
        a = 1
        b = 2
        while i<=number:
            result = a + b
            a = b
            b = result
            i += 1
        return result

import time
if __name__ == "__main__":
    input = 100
    s = Solution()
    t0 = time.time()
    result = s.rectCover(input)
    print('result = {}, run time: {}'.format(result, time.time()-t0))
