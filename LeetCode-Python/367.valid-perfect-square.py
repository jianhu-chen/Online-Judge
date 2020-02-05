# -*- encoding: utf-8 -*-
'''
@File    :   367.valid-perfect-square.py
@Time    :   2020/02/05 23:42:55
@Author  :   jhchen
@E-mail  :   jianhuchen@163.com
@License :   Copyright(C), USTC
@Desc    :   None
'''
#
# @lc app=leetcode id=367 lang=python
#
# [367] Valid Perfect Square
#

# @lc code=start
class Solution(object):
    def isPerfectSquare(self, num):
        """方法1：暴力法 超时
        :type num: int
        :rtype: bool
        """
        for i in range(int(num/2)+2, 0, -1):
            if i ** 2 == num:
                return True
        return False
    
    def isPerfectSquare(self, num):
        """方法2：二分查找 O(log(n))
        :type num: int
        :rtype: bool
        """
        if num == 1:
            return True
        left, right = 0, num // 2
        while left <= right:
            center = (left + right) // 2
            square = center ** 2
            if square == num:
                return True
            if square > num:
                right = center - 1
            else:
                left = center + 1
        return False
        
# @lc code=end
if __name__ == "__main__":
    r = Solution().isPerfectSquare(9)
    print(r)
