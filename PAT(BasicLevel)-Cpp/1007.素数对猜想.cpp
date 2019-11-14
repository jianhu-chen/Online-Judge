//
// Created by jhchen<jianhuchen@163.com> on 2019-11-12 15:03:32.
//
// 题目链接: https://pintia.cn/problem-sets/994805260223102976/problems/994805317546655744
// 题目描述: 让我们定义$$d_n$$为：$$d_n = p_{n+1}-p_n$$，其中$$p_i$$是第$$i$$个素数。显然有$$d_1 = 1$$，且对于$$n>1$$有$$d_n$$是偶数。“素数对猜想”认为“存在无穷多对相邻且差为2的素数”。
// 
// 现给定任意正整数`N`($$<10^5$$)，请计算不超过`N`的满足猜想的素数对的个数。
// 
// 
// ### 输入格式:
// 
// 输入在一行给出正整数`N`。
// 
// ### 输出格式:
// 
// 在一行中输出不超过`N`的满足猜想的素数对的个数。
// 
// ### 输入样例:
// ```in
// 20
// ```
// 
// ### 输出样例:
// ```out
// 4
// 
#include <iostream>
#include <cmath>

using namespace std;

bool isSushu(int n) {
    for (int i = 2; i <= sqrt(n); ++i) {
        if (n % i == 0) {
            return false;
        }
    }
    return true;
}

int main() {
    int n = 3, pre = 2, N, count = 0;
    scanf("%d", &N);
    while (n <= N) {
        if (isSushu(n)) {
            if (n - pre == 2) {
                ++count;
            }
            pre = n;
        }
        ++n;
    }
    printf("%d", count);
    return 0;
}
            