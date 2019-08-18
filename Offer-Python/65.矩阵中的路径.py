## 题目描述
# 请设计一个函数，用来判断在一个矩阵中是否存在一条包含某字符串所有字符的路径。
# 路径可以从矩阵中的任意一个格子开始，每一步可以在矩阵中向左，向右，向上，向下移动一个格子。
# 如果一条路径经过了矩阵中的某一个格子，则之后不能再次进入这个格子。 
# 例如 a b c e s f c s a d e e 这样的3 X 4 矩阵中包含一条字符串"bcced"的路径，
# 但是矩阵中不包含"abcb"路径，因为字符串的第一个字符b占据了矩阵中的第一行第二个格子之后，
# 路径不能再次进入该格子。

# -*- coding:utf-8 -*-
class Solution:
    def hasPath(self, matrix, rows, cols, path):
        # write code here
        if rows < 0 or cols < 0 or not matrix or not path:
            return False 
        index = 0
        visited = [False for _ in range(len(matrix))]
        for i in range(rows):
            for j in range(cols):
                if self.hasPathCore(matrix, rows, cols, i, j, index, path, visited):
                    return True
        return False

    def hasPathCore(self, matrix, rows, cols, i, j, index, path, visited):
        if index == len(path):
            return True
        if i >= 0 and j >= 0 and i < rows and j < cols and matrix[i * cols + j] == path[index] and not visited[i * cols + j]:
            visited[i * cols + j] = True
            index += 1
            has_path =  (self.hasPathCore(matrix, rows, cols, i-1, j, index, path, visited) or \
                        self.hasPathCore(matrix, rows, cols, i+1, j, index, path, visited) or \
                        self.hasPathCore(matrix, rows, cols, i, j-1, index, path, visited) or \
                        self.hasPathCore(matrix, rows, cols, i, j+1, index, path, visited) )
            if not has_path:
                index -= 1
                visited[i * cols + j] = False
            else:
                return True
        return False

if __name__ == "__main__":
    s = Solution()
    result = s.hasPath("AAAAAAAAAAAA", 3, 4, "AAAAAAAAAAAA")
    print(result)
