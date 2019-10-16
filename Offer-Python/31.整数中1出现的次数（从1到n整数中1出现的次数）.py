## 题目描述
# 求出1~13的整数中1出现的次数,并算出100~1300的整数中1出现的次数？
# 为此他特别数了一下1~13中包含1的数字有1、10、11、12、13因此共出现6次,但是对于后面问题他就没辙了。
# ACMer希望你们帮帮他,并把问题更加普遍化,可以很快的求出任意非负整数区间中1出现的次数（从1 到 n 中1出现的次数）。


# -*- coding:utf-8 -*-
class Solution:
    # def NumberOf1Between1AndN_Solution(self, n):
    #     # write code here
    #     if n<1:
    #         return 0
    #     sum = 0
    #     for i in range(1, n+1):
    #         sum += list(str(i)).count('1')
    #     return sum

    # 方法二
    def NumberOf1Between1AndN_Solution(self, n):
        if n < 1:
            return 0
        count = 0
        for i in range(1, n+1):
            t = i
            while t:
                if (t-1)%10 == 0:
                    count += 1
                t = t // 10
        return count



if __name__ == "__main__":
    n = 10
    S = Solution()
    rst = S.NumberOf1Between1AndN_Solution(n)
    print(rst)