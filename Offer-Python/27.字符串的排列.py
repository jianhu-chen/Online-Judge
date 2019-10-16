## 题目描述
# 输入一个字符串,按字典序打印出该字符串中字符的所有排列。
# 例如输入字符串abc,则打印出由字符a,b,c所能排列出来的所有字符串abc,acb,bac,bca,cab和cba。

# 输入描述:
# 输入一个字符串,长度不超过9(可能有字符重复),字符只包括大小写字母。

# 方法1：调用itertools库
# -*- coding:utf-8 -*-
# import itertools
# class Solution:
#     def Permutation(self, ss):
#         # write code here
#         if not ss:
#             return []
#         enum = itertools.permutations(ss)
#         enum = map(''.join, enum)
#         enum = sorted(list(set(enum)))
#         return enum

# 方法2: 递归
class Solution:
    def Permutation(self, ss):
        # write code here
        if not ss:
            return []
        if len(ss) == 1:
            return ss
        result = []
        s = ss[0]
        for ii in self.Permutation(ss[1:]):
            for j in range(len(ii)+1):
                result.append(ii[:j]+s+ii[j:])
        result = list(set(result))
        result.sort()
        return result



if __name__ == "__main__":
    ss = 'abc'
    S = Solution()
    rst = S.Permutation(ss)
    print(rst)