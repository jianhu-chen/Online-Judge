## 题目描述
# 每年六一儿童节,牛客都会准备一些小礼物去看望孤儿院的小朋友,
# 今年亦是如此。HF作为牛客的资深元老,自然也准备了一些小游戏。
# 其中,有个游戏是这样的:首先,让小朋友们围成一个大圈。
# 然后,他随机指定一个数m,让编号为0的小朋友开始报数。
# 每次喊到m-1的那个小朋友要出列唱首歌,然后可以在礼品箱中任意的挑选礼物,
# 并且不再回到圈中,从他的下一个小朋友开始,继续0...m-1报数....这样下去...
# 直到剩下最后一个小朋友,可以不用表演,并且拿到牛客名贵的“名侦探柯南”典藏版(名额有限哦!!^_^)。
# 请你试着想下,哪个小朋友会得到这份礼品呢？(注：小朋友的编号是从0到n-1)

# -*- coding:utf-8 -*-
class Solution:
    def LastRemaining_Solution(self, n, m):
        # write code here
        # 方法一：模拟法
        # if n <= 1:
        #     return -1
        # p = 0 # 指向报数的学生
        # num = 0 # 当前正在报的数
        # childs = [1 for _ in range(n)]
        # while sum(childs) > 1:
        #     while not childs[p]:
        #         p = (p + 1) % n
        #     if num == m-1:
        #         childs[p] = 0 # 退出游戏
        #         num = 0
        #     else:
        #         num += 1
        #     p = (p + 1) % n
        # return childs.index(1)
        # 方法二：数学归纳法
        if n < 1 or m < 1:
            return -1
        last = 0
        for i in range(2,n+1):
            last = (last + m) % i
        return last

if __name__ == "__main__":
    n = 10
    m = 1
    s = Solution()
    result = s.LastRemaining_Solution(n, m)
    print(result)
