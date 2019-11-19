# -*- encoding: utf-8 -*-
'''
@File    :   125.valid-palindrome.py
@Time    :   2019/11/19 23:00:33
@Author  :   jhchen
@E-mail  :   jianhuchen@163.com
@License :   Copyright(C), USTC
@Desc    :   None
'''
#
# @lc app=leetcode id=125 lang=python
#
# [125] Valid Palindrome
#
# https://leetcode.com/problems/valid-palindrome/description/
#
# algorithms
# Easy (32.90%)
# Likes:    762
# Dislikes: 2222
# Total Accepted:    441.4K
# Total Submissions: 1.3M
# Testcase Example:  '"A man, a plan, a canal: Panama"'
#
# Given a string, determine if it is a palindrome, considering only
# alphanumeric characters and ignoring cases.
#
# Note: For the purpose of this problem, we define empty string as valid
# palindrome.
#
# Example 1:
#
#
# Input: "A man, a plan, a canal: Panama"
# Output: true
#
#
# Example 2:
#
#
# Input: "race a car"
# Output: false
#
#
#

# @lc code=start
import re


class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        alphanumeric = ''.join(re.findall(r'[A-Za-z0-9]', s)).upper()
        if alphanumeric == alphanumeric[::-1]:
            return True
        return False

# @lc code=end
