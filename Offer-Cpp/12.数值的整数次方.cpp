//
// Created by 陈建虎 on 2019-11-04.
//
//题目描述
//给定一个double类型的浮点数base和int类型的整数exponent。求base的exponent次方。
//保证base和exponent不同时为0
//
#include <iostream>
#include <cmath>

using namespace std;

class Solution {
public:
    double Power(double base, int exponent) {
        if (base == 0) {
            return 0;
        }
        if (exponent == 0) {
            return 1;
        }
        return pow(base, exponent);
    }
};