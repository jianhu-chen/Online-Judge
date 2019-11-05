//
// Created by 陈建虎 on 2019-11-05.
//
// 题目描述
// 输入一个矩阵，按照从外向里以顺时针的顺序依次打印出每一个数字，例如，
// 如果输入如下4 X 4矩阵： 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16
// 则依次打印出数字1,2,3,4,8,12,16,15,14,13,9,5,6,7,11,10.

#include <iostream>
#include <vector>

using namespace std;

class Solution {
public:
    vector<int> printMatrix(vector<vector<int> > matrix) {
        auto rst = vector<int>();
        int rows = matrix.size();
        int cols = matrix[0].size();
        int left = 0;
        int right = cols - 1;
        int top = 0;
        int bottom = rows - 1;
        while (left <= right && top <= bottom) {
            for (int i = left; i <= right; ++i) {
                rst.push_back(matrix[top][i]);
            }
            for (int i = top + 1; i <= bottom; ++i) {
                rst.push_back(matrix[i][right]);
            }
            // 一行的特殊情况
            if (top != bottom) {
                for (int i = right - 1; i > left - 1; --i) {
                    rst.push_back(matrix[bottom][i]);
                }
            }
            // 一列的特殊情况
            if (left != right) {
                for (int i = bottom - 1; i > top; --i) {
                    rst.push_back(matrix[i][left]);
                }
            }
            left += 1;
            right -= 1;
            top += 1;
            bottom -= 1;
        }

        return rst;
    }
};