//
// Created by 陈建虎 on 2019-11-04.
//
//题目描述
//我们可以用2*1的小矩形横着或者竖着去覆盖更大的矩形。请问用n个2*1的小矩形无重叠地覆盖一个2*n的大矩形，总共有多少种方法？

#include <iostream>
#include <map>

using namespace std;

// 动态规划
class Solution {
public:
    int rectCover(int number) {
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