## 题目描述
# 把只包含质因子2、3和5的数称作丑数（Ugly Number）。
# 例如6、8都是丑数，但14不是，因为它包含质因子7。 
# 习惯上我们把1当做是第一个丑数。求按从小到大的顺序的第N个丑数。

# -*- coding:utf-8 -*-
class Solution:
    def GetUglyNumber_Solution(self, index):
        # write code here
        if index<=0:
            return 0
        if index == 1:
            return 1
        ugly_list = [1]
        index_2 = 0
        index_3 = 0
        index_5 = 0
        for i in range(index-1):
            new_ugly = min(ugly_list[index_2]*2, ugly_list[index_3]*3, ugly_list[index_5]*5)
            ugly_list.append(new_ugly)
            if new_ugly%2 == 0:
                index_2 += 1
            if new_ugly%3 == 0:
                index_3 += 1
            if new_ugly%5 == 0:
                index_5 += 1
        print(ugly_list)
        return ugly_list[index-1]

if __name__ == "__main__":
    n = 9999
    solution = Solution()
    ret = solution.GetUglyNumber_Solution(n)
    print(ret)