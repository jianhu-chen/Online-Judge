//
// Created by 陈建虎 on 2019-11-05.
//
// 题目描述
// HZ偶尔会拿些专业问题来忽悠那些非计算机专业的同学。今天测试组开完会后,他又发话了:在古老的一维模式识别中,
// 常常需要计算连续子向量的最大和,当向量全为正数的时候,问题很好解决。但是,如果向量中包含负数,是否应该包含
// 某个负数,并期望旁边的正数会弥补它呢？例如:{6,-3,-2,7,-15,1,2,2},连续子向量的最大和为8(从第0个开始,
// 到第3个为止)。给一个数组，返回它的最大连续子序列的和，你会不会被他忽悠住？(子向量的长度至少是1)

#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

//使用动态规划
//F（i）：以array[i]为末尾元素的子数组的和的最大值，子数组的元素的相对位置不变
//F（i）=max（F（i-1）+array[i] ， array[i]）
//res：所有子数组的和的最大值
//res=max（res，F（i））
class Solution {
public:
    int FindGreatestSumOfSubArray(vector<int> array) {
        int result = array[0];
        int fi_1 = array[0];
        for (int i = 1; i < array.size(); ++i) {
            int fi = max(fi_1 + array[i], array[i]);
            if (fi > result) {
                result = fi;
            }
            fi_1 = fi;
        }
        return result;
    }
};