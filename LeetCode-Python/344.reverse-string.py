# -*- encoding: utf-8 -*-
'''
@File    :   344.reverse-string.py
@Time    :   2020/02/05 23:26:46
@Author  :   jhchen
@E-mail  :   jianhuchen@163.com
@License :   Copyright(C), USTC
@Desc    :   None
'''
#
# @lc app=leetcode id=344 lang=python
#
# [344] Reverse String
#

# @lc code=start
class Solution(object):
    def reverseString(self, s):
        """
        :type s: List[str]
        :rtype: None Do not return anything, modify s in-place instead.
        """
        if not s:
            return []
        front_idx = 0
        end_idx = len(s) - 1

        while front_idx < end_idx:
            s[front_idx], s[end_idx] = s[end_idx], s[front_idx]
            front_idx += 1
            end_idx -= 1
    
    def reverseString(self, s):
        s.reverse()

# @lc code=end
if __name__ == "__main__":
    s = ["h","e","l","l","o"]
    Solution().reverseString(s)
    print(s)
