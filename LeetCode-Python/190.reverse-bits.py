# -*- encoding: utf-8 -*-
'''
@File    :   190.reverse-bits.py
@Time    :   2020/01/30 19:54:26
@Author  :   jhchen
@E-mail  :   jianhuchen@163.com
@License :   Copyright(C), USTC
@Desc    :   None
'''
#
# @lc app=leetcode id=190 lang=python
#
# [190] Reverse Bits
#

# @lc code=start
class Solution:
    # @param n, an integer
    # @return an integer
    # def reverseBits(self, n):
    #     """方法一
    #     """
    #     bin_str = bin(n)[2:]
    #     front_zero = "0" * (32 - len(bin_str))
    #     bin_str = front_zero + bin_str
    #     return int(bin_str[::-1], 2)

    def reverseBits(self, n):
        """方法二
        """
        result = 0
        for i in range(32):
            result <<= 1
            result += n & 1
            n >>= 1
        return result
        
# @lc code=end

if __name__ == "__main__":
    r = Solution().reverseBits(43261596)
    print(r)