# -*- coding:utf-8 -*-
class Solution:
    # matrix类型为二维列表，需要返回列表
    def printMatrix(self, matrix):
        # write code here
        rows = len(matrix)
        cols = len(matrix[0])
        if rows == 0 or cols == 0: # 可能有x行，0列的情况 [[], [], []] 3*0
            return []
        left, right, top, bottom = 0, cols-1, 0, rows-1
        result = []
        while left <= right and top <= bottom:
            for i in range(left, right+1):
                result.append(matrix[top][i])
            for i in range(top+1, bottom+1):
                result.append(matrix[i][right])
            if top != bottom: # 一行的特殊情况
                for i in range(right-1, left-1, -1):
                    result.append(matrix[bottom][i])
            if left != right: # 一列的特殊情况
                for i in range(bottom-1, top, -1):
                    result.append(matrix[i][left])
            left += 1
            right -= 1
            top += 1
            bottom -= 1
        return result

if __name__ == "__main__":
    # data = [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12], [13, 14, 15, 16]]
    # data = [[1, 2], [3, 4]]
    # data = [[1]]
    data = [[1],[2],[3],[4],[5]]
    # data = [[1, 2, 3, 4, 5]]
    S = Solution()
    result = S.printMatrix(data)
    print(result)
    # 1,2,3,4,8,12,16,15,14,13,9,5,6,7,11,10.