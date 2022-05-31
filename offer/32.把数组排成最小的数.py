## 题目描述
# 输入一个正整数数组，把数组里所有数字拼接起来排成一个数，打印能拼接出的所有数字中最小的一个。
# 例如输入数组{3，32，321}，则打印出这三个数字能排成的最小数字为321323。


# 方法1：使用itertools库
# -*- coding:utf-8 -*-
# import itertools
# class Solution:
#     def PrintMinNumber(self, numbers):
#         # write code here
#         if not numbers:
#             return ""
#         str_list = [str(i) for i in numbers]
#         l = sorted(set(map(''.join, itertools.permutations(str_list))))
#         return int(l[0])

# 方法2：递归
import copy
class Solution:
    def PrintMinNumber(self, numbers):
        # write code here
        if not numbers:
            return ''
        numbers = [str(n) for n in numbers]
        result = self.MinNumber(numbers)
        result_int = [eval(''.join(r)) for r in result]
        return min(result_int)

    def MinNumber(self, numbers):
        if len(numbers) == 1:
            return [[numbers[0], ]]
        result =[]
        n = numbers[0]
        for nums in self.MinNumber(numbers[1:]):
            for i in range(len(nums)+1):
                nums_copy = copy.deepcopy(nums)
                nums_copy.insert(i, n)
                result.append(nums_copy)
        return result

if __name__ == "__main__":
    numbers = [3, 32, 321]
    S = Solution()
    rst = S.PrintMinNumber(numbers)
    print(rst)