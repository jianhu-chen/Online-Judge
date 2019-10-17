## 题目描述
# 将一个字符串转换成一个整数(实现Integer.valueOf(string)的功能，但是string不符合数字要求时返回0)，
# 要求不能使用字符串转换整数的库函数。 数值为0或者字符串不是一个合法的数值则返回0。

# 输入描述:
# > 输入一个字符串,包括数字字母符号,可以为空

# 输出描述:
# > 如果是合法的数值表达则返回该数字，否则返回0


# -*- coding:utf-8 -*-
class Solution:
    def StrToInt(self, s):
        # write code here
        if s=='':
            return 0
        # 处理符号
        sign = 'None'
        if s[0]=='+' or s[0]=='-':
            sign = s[0]
        if sign != 'None':
            s = s.replace('+', '').replace('-', '')
        # 判断是否为数字
        if not s.isdigit():
            return 0
        res = 0
        for i in range(len(s)):
            res += (int(s[i])) * (10**(len(s)-i-1))
        if sign == "-":
            return -res
        else:
            return res
