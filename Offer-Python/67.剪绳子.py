## 题目描述
# 给你一根长度为n的绳子，请把绳子剪成m段（m、n都是整数，n>1并且m>1），每段绳子的长度记为k[0],k[1],...,k[m]。请问k[0]xk[1]x...xk[m]可能的最大乘积是多少？例如，当绳子的长度是8时，我们把它剪成长度分别为2、3、3的三段，此时得到的最大乘积是18。
# 输入描述:
# 输入一个数n，意义见题面。（2 <= n <= 60）
# 输出描述:
# 输出答案。
#
# 示例1
# 输入
# 8
# 输出
# 18

# -*- coding:utf-8 -*-
class Solution:
    def cutRope(self, number):
        # write code here
        # 方法一：贪婪算法
        # if number < 2: # 
        #     return 0
        # if number == 2: # 1, 1
        #     return 1
        # if number == 3: # 1, 2
        #     return 2

        # times_of_3 = int(number / 3)
        
        # if number - times_of_3 * 3 == 1:
        #     times_of_3 -= 1
        
        # times_of_2 = (number - times_of_3 * 3) / 2

        # return 3 ** times_of_3 * 2 ** times_of_2
        
        # 方法二：动态规划
        if number < 2: # 
            return 0
        if number == 2: # 1, 1
            return 1
        if number == 3: # 1, 2
            return 2

        products = [i for i in range(number+1)]

        for i in range(4, number+1):
            max_ = 0
            for j in range(1, int(i/2)+1):
                product = products[j] * products[i - j]
                if product > max_:
                    max_ = product
            products[i] = max_
        
        max_ = products[number]
        return max_


if __name__ == "__main__":
    number = 4
    s =Solution()
    result =  s.cutRope(number)
    print(result)