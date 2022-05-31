## 题目描述
# 地上有一个m行和n列的方格。一个机器人从坐标0,0的格子开始移动，
# 每一次只能向左，右，上，下四个方向移动一格，但是不能进入行坐标
# 和列坐标的数位之和大于k的格子。 
# 
# 例如，当k为18时，机器人能够进入方格（35,37），因为3+5+3+7 = 18。
# 但是，它不能进入方格（35,38），因为3+5+3+8 = 19。请问该机器人能够达到多少个格子？

# -*- coding:utf-8 -*-
class Solution:
    def movingCount(self, threshold, rows, cols):
        # write code here
        if threshold <= 0:
            return 0
        visited = [0 for _ in range(rows * cols)]
        self.moving(0, 0, rows, cols, threshold, visited)
        return sum(visited)

    def moving(self, i, j, rows, cols, threshold, visited):
        if self.getSum(i) + self.getSum(j) > threshold:
            return
        if i >= 0 and j >= 0 and i < rows and j < cols and visited[i * cols + j] == 0:
            visited[i * cols + j] = 1
            self.moving(i-1, j, rows, cols, threshold, visited)
            self.moving(i+1, j, rows, cols, threshold, visited)
            self.moving(i, j-1, rows, cols, threshold, visited)
            self.moving(i, j+1, rows, cols, threshold, visited)

    def getSum(self, n):
        if n < 0:
            return 0
        sum = 0
        while n != 0:
            unit = n % 10
            sum += unit
            n //= 10
        return sum

if __name__ == "__main__":
    s =Solution()
    result =  s.movingCount(5, 20, 20)
    print(result)