//
// Created by 陈建虎 on 2019-11-05.
//
//题目描述
//输入n个整数，找出其中最小的K个数。例如输入4,5,1,6,2,7,3,8这8个数字，则最小的4个数字是1,2,3,4,。

#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

class Solution {
public:
    vector<int> GetLeastNumbers_Solution(vector<int> input, int k) {
        if (k < 0 || k > input.size()) {
            return vector<int>();
        }
        sort(input.begin(), input.end());
        input.resize(k);
        return input;
    }
};