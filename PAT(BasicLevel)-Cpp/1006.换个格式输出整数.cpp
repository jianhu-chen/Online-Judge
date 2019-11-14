//
// Created by jhchen<jianhuchen@163.com> on 2019-11-12 15:03:31.
//
// 题目链接: https://pintia.cn/problem-sets/994805260223102976/problems/994805318855278592
// 题目描述: 让我们用字母 `B` 来表示“百”、字母 `S` 表示“十”，用 `12...n` 来表示不为零的个位数字 `n`（$$<10$$），换个格式来输出任一个不超过 3 位的正整数。例如 `234` 应该被输出为 `BBSSS1234`，因为它有 2 个“百”、3 个“十”、以及个位的 4。
// 
// ### 输入格式：
// 
// 每个测试输入包含 1 个测试用例，给出正整数 $$n$$（$$<1000$$）。
// 
// ### 输出格式：
// 
// 每个测试用例的输出占一行，用规定的格式输出 $$n$$。
// 
// ### 输入样例 1：
// ```in
// 234
// ```
// 
// ### 输出样例 1：
// ```out
// BBSSS1234
// ```
// 
// ### 输入样例 2：
// ```in
// 23
// ```
// 
// ### 输出样例 2：
// ```out
// SS123
// ```

#include <iostream>
#include <string>

using namespace std;

int main() {
    int num;
    string result;
    cin >> num;
    for (int i = 0; num != 0; ++i, num /= 10) {
        int unit = num % 10;

        if (i == 0) { // 个位
            for (int j = unit; j > 0; --j) {
                result = to_string(j) + result;
            }
        }

        if (i == 1) {
            result = string(unit, 'S') + result;
        }

        if (i == 2) {
            result = string(unit, 'B') + result;
        }
    }
    cout << result;
    return 0;
}
            