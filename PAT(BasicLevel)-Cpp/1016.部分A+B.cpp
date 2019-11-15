//
// Created by jhchen<jianhuchen@163.com> on 2019-11-12 15:03:36.
//
// 题目链接: https://pintia.cn/problem-sets/994805260223102976/problems/994805306310115328
// 题目描述: 正整数 $$A$$ 的“$$D_A$$（为 1 位整数）部分”定义为由 $$A$$ 中所有 $$D_A$$ 组成的新整数 $$P_A$$。例如：给定 $$A = 3862767$$，$$D_A = 6$$，则 $$A$$ 的“6 部分”$$P_A$$ 是 66，因为 $$A$$ 中有 2 个 6。
// 
// 现给定 $$A$$、$$D_A$$、$$B$$、$$D_B$$，请编写程序计算 $$P_A + P_B$$。
// 
// ### 输入格式：
// 
// 输入在一行中依次给出 $$A$$、$$D_A$$、$$B$$、$$D_B$$，中间以空格分隔，其中 $$0 < A, B < 10^{10}$$。
// 
// ### 输出格式：
// 
// 在一行中输出 $$P_A + P_B$$ 的值。
// 
// ### 输入样例 1：
// ```in
// 3862767 6 13530293 3
// ```
// 
// ### 输出样例 1：
// ```out
// 399
// ```
// 
// ### 输入样例 2：
// ```in
// 3862767 1 13530293 8
// ```
// 
// ### 输出样例 2：
// ```out
// 0
// ```

#include <iostream>
#include<cmath>

using namespace std;

int getPNumber(int N, int DN) {
    int DNCount = 0, result = 0;
    while (N != 0) {
        if (N % 10 == DN) {
            ++DNCount;
        }
        N /= 10;
    }
    for (int i = 0; i < DNCount; ++i) {
        result += (DN * pow(10, i));
    }
    return result;
}

int main() {
    int A, DA, B, DB, PA, PB, DACount = 0, DBCount = 0;
    cin >> A >> DA >> B >> DB;
    PA = getPNumber(A, DA);
    PB = getPNumber(B, DB);
    cout << PA + PB;
    return 0;
}
            