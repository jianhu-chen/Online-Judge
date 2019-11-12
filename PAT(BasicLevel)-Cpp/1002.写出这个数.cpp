//
// Created by jhchen<jianhuchen@163.com> on 2019-11-12 15:03:27.
//
// 题目链接: https://pintia.cn/problem-sets/994805260223102976/problems/994805324509200384
// 题目描述: 读入一个正整数 $$n$$，计算其各位数字之和，用汉语拼音写出和的每一位数字。
// 
// ### 输入格式：
// 
// 每个测试输入包含 1 个测试用例，即给出自然数 $$n$$ 的值。这里保证 $$n$$ 小于 $$10^{100}$$。
// 
// ### 输出格式：
// 
// 在一行内输出 $$n$$ 的各位数字之和的每一位，拼音数字间有 1 空格，但一行中最后一个拼音数字后没有空格。
// 
// ### 输入样例：
// ```in
// 1234567890987654321123456789
// ```
// 
// ### 输出样例：
// ```out
// yi san wu
// ```

#include <iostream>
#include <string>

using namespace std;

int main() {
    string str_n;
    string nums[10] = {"ling", "yi", "er", "san", "si", "wu", "liu", "qi", "ba", "jiu"};
    int sum = 0;
    cin >> str_n;
    for (int i = 0; i < str_n.size(); ++i) {
        sum += (str_n[i] - '0');
    }

    string result;
    string str_sum = to_string(sum);
    for (int i = 0; i < str_sum.size(); ++i) {
        result += (nums[str_sum[i] - '0'] + " ");
    }
    result.erase(result.size() - 1, 1);
    cout << result;
    return 0;
}