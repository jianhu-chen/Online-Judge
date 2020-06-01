# -*- encoding: utf-8 -*-
'''
@File    :   5.longest-palindromic-substring.py
@Time    :   2020/05/31 22:10:29
@Author  :   jhchen
@E-mail  :   jianhuchen@163.com
@License :   Copyright(C), USTC
@Desc    :   None
'''
#
# @lc app=leetcode id=5 lang=python
#
# [5] Longest Palindromic Substring
#


# @lc code=start
def is_palindromic(s):
    length = len(s)
    if length <= 1:
        return True
    p_i, p_j = 0, length - 1
    while p_i < p_j:
        if s[p_i] != s[p_j]:
            return False
        p_i += 1
        p_j -= 1
    return True


class Solution(object):
    def longestPalindrome(self, s):
        """
        方法1: 暴力破解
        :type s: str
        :rtype: str
        """
        length = len(s)
        if length <= 1:
            return s

        ret = ""
        for i in range(length):
            for j in range(i, length):
                if is_palindromic(s[i:j+1]) and len(ret) < (j-i+1):
                    ret = s[i: j+1]
        return ret

    def longestPalindrome(self, s):
        """
        方法2: 
        :type s: 动态规划
        :rtype: str
        """
        length = len(s)
        if length <= 1:
            return s

        dp = [[False] * length for _ in range(length)]
        ret = ""
        # 枚举长度
        for l in range(1, length + 1):
            # 枚举子串的起始位置
            for i in range(length):
                j = i + l - 1
                if j >= length:
                    break
                if l == 1:
                    dp[i][j] = True
                elif l == 2:
                    dp[i][j] = (s[i] == s[j])
                else:
                    dp[i][j] = (s[i] == s[j]) and dp[i+1][j-1]
                if dp[i][j] and l > len(ret):
                    ret = s[i: j+1]
        return ret
# @lc code=end
