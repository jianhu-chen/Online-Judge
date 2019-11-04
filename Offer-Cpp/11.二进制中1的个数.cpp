//
// Created by 陈建虎 on 2019-11-04.
//
//题目描述
//输入一个整数，输出该数二进制表示中1的个数。其中负数用补码表示。

#include <iostream>

using namespace std;

class Solution {
public:
    int NumberOf1(int n) {
        int count = 0;
        unsigned int flag = 1;
        while (flag) {
            if (n & flag) {
                ++count;
            }
            flag = flag << 1;
        }
        return count;
    }
};

int main() {
    unsigned int flag = 1;
    cout << (2 & flag<<1);
    return 0;
}
