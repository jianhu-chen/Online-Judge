# -*- encoding: utf-8 -*-
'''
@File    :   202.happy-number.py
@Time    :   2020/01/30 22:41:07
@Author  :   jhchen
@E-mail  :   jianhuchen@163.com
@License :   Copyright(C), USTC
@Desc    :   None
'''
#
# @lc app=leetcode id=202 lang=python
#
# [202] Happy Number
#

# @lc code=start
class Solution(object):
    def isHappy(self, n):
        """快慢指针法
        :type n: int
        :rtype: bool
        """
        fast = n
        slow = n
        while True:
            slow = self.sum_of_squares(slow)
            fast = self.sum_of_squares(fast)
            fast = self.sum_of_squares(fast)
            if slow == fast:
                break
        if fast == 1:
            return True
        else:
            return False

    def sum_of_squares(self, n):
        result = 0
        while n:
            result += (n % 10) ** 2
            n //= 10
        return result
# @lc code=end
if __name__ == "__main__":
    r = Solution().sum_of_squares(19)
    print(r)
