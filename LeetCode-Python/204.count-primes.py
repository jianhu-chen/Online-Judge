# -*- encoding: utf-8 -*-
'''
@File    :   204.count-primes.py
@Time    :   2020/01/31 00:23:28
@Author  :   jhchen
@E-mail  :   jianhuchen@163.com
@License :   Copyright(C), USTC
@Desc    :   None
'''
#
# @lc app=leetcode id=204 lang=python
#
# [204] Count Primes
#

# @lc code=start
class Solution(object):
    # def countPrimes(self, n):
    #     """方法一：暴力，超时
    #     :type n: int
    #     :rtype: int
    #     """
    #     if n == 1 or n == 2:
    #         return 0
    #     count = 0
    #     for i in range(2, n):
    #         if self.isPrime(i):
    #             count += 1
    #     return count

    def countPrimes(self, n):
        """方法2：
        ref: https://pic.leetcode-cn.com/23d348bef930ca4bb73f749500f664ccffc5e41467aac0ba9787025392ca207b-1.gif
        :type n: int
        :rtype: int
        """
        if n < 2:
            return 0
        array = [True] * n
        array[0] = array[1] = False
        for i in range(2, int(n ** 0.5) + 1):
            if array[i] and self.isPrime(i):
                array[i*i:n:i] = [False] * len(array[i*i:n:i])
        return sum(array)

    def isPrime(self, n):
        if n <= 1:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True
# @lc code=end
if __name__ == "__main__":
    r = Solution().isPrime(2)
    print(r)
