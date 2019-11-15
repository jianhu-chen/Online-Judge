//
// Created by jhchen<jianhuchen@163.com> on 2019-11-12 15:03:36.
//
// 题目链接: https://pintia.cn/problem-sets/994805260223102976/problems/994805308755394560
// 题目描述: 大侦探福尔摩斯接到一张奇怪的字条：`我们约会吧！ 3485djDkxh4hhGE 2984akDfkkkkggEdsb s&hgsfdk d&Hyscvnm`。大侦探很快就明白了，字条上奇怪的乱码实际上就是约会的时间`星期四 14:04`，因为前面两字符串中第 1 对相同的大写英文字母（大小写有区分）是第 4 个字母 `D`，代表星期四；第 2 对相同的字符是 `E` ，那是第 5 个英文字母，代表一天里的第 14 个钟头（于是一天的 0 点到 23 点由数字 0 到 9、以及大写字母 `A` 到 `N` 表示）；后面两字符串第 1 对相同的英文字母 `s` 出现在第 4 个位置（从 0 开始计数）上，代表第 4 分钟。现给定两对字符串，请帮助福尔摩斯解码得到约会的时间。
// 
// ### 输入格式：
// 
// 输入在 4 行中分别给出 4 个非空、不包含空格、且长度不超过 60 的字符串。
// 
// ### 输出格式：
// 
// 在一行中输出约会的时间，格式为 `DAY HH:MM`，其中 `DAY` 是某星期的 3 字符缩写，即 `MON` 表示星期一，`TUE` 表示星期二，`WED` 表示星期三，`THU` 表示星期四，`FRI` 表示星期五，`SAT` 表示星期六，`SUN` 表示星期日。题目输入保证每个测试存在唯一解。
// 
// ### 输入样例：
// ```in
// 3485djDkxh4hhGE 
// 2984akDfkkkkggEdsb 
// s&hgsfdk 
// d&Hyscvnm
// ```
// 
// ### 输出样例：
// ```out
// THU 14:04
// ```

#include <iostream>
#include <string>
#include <algorithm>

using namespace std;

int main() {
    int HH, MM, i = 0, j = 0;
    string week[7] = {"MON", "TUE", "WED", "THU", "FRI", "SAT", "SUN"};
    string DAY, str1_1, str1_2, str2_1, str2_2;;

    cin >> str1_1 >> str1_2 >> str2_1 >> str2_2;
    while (i < min(str1_1.length(), str1_2.length())) {
        if (str1_1[i] == str1_2[i] && str1_1[i] >= 'A' && str1_1[i] <= 'G') {
            DAY = week[str1_1[i] - 'A'];
            break;
        }
        ++i;
    }
    ++i;
    while (i < min(str1_1.length(), str1_2.length())) {
        if (str1_1[i] == str1_2[i] && (isdigit(str1_1[i]) || (str1_1[i] >= 'A' && str1_1[i] <= 'N'))) {
            HH = isdigit(str1_1[i]) ? str1_1[i] - '0' : str1_1[i] - 'A' + 10;
            break;
        }
        ++i;
    }
    while (j < min(str2_1.length(), str2_2.length())) {
        if (str2_1[j] == str2_2[j] && isalpha(str2_1[j])) {
            MM = j;
            break;
        }
        ++j;
    }

    cout << DAY;
    printf(" %02d:%02d", HH, MM);

    return 0;
}
            