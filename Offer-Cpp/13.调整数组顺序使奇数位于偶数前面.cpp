//
// Created by 陈建虎 on 2019-11-04.
//
// 题目描述
// 输入一个整数数组，实现一个函数来调整该数组中数字的顺序，使得所有的奇数位于数组的前半部分，
// 所有的偶数位于数组的后半部分，并保证奇数和奇数，偶数和偶数之间的相对位置不变。

#include <iostream>
#include <vector>

using namespace std;

// 分两个数组，再拼接
class Solution {
public:
    void reOrderArray(vector<int> &array) {
        vector<int> ji, ou;
        for (auto it = array.begin(); it != array.end(); it++) {
            if (*it % 2 == 0) {
                ou.push_back(*it);
            } else {
                ji.push_back(*it);
            }
        }
        for (auto it = ou.begin(); it != ou.end(); it++) {
            ji.push_back(*it);
        }
        array.swap(ji);
    }
};
