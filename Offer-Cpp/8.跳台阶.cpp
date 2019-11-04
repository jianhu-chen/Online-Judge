//
// Created by 陈建虎 on 2019-11-04.
//
// 题目描述
// 一只青蛙一次可以跳上1级台阶，也可以跳上2级。求该青蛙跳上一个n级的台阶总共有多少种跳法（先后次序不同算不同的结果）。

#include <iostream>
#include <map>

using namespace std;

// 动态规划
class Solution {
public:
    int jumpFloor(int number) {
        if (number == 0) {
            return 0;
        }

        map<int, int> dict;
        dict.insert(make_pair(1, 1));
        dict.insert(make_pair(2, 2));

        for (int i = 3; i <= number; i++) {
            dict.insert(make_pair(i, dict[i - 1] + dict[i - 2]));
        }

        return dict[number];
    }
};