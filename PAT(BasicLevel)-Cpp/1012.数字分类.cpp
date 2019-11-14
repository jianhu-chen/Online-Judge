//
// Created by jhchen<jianhuchen@163.com> on 2019-11-12 15:03:35.
//
// 题目链接: https://pintia.cn/problem-sets/994805260223102976/problems/994805311146147840
// 题目描述: 给定一系列正整数，请按要求对数字进行分类，并输出以下 5 个数字：
// 
// - $$A_1$$ = 能被 5 整除的数字中所有偶数的和；
// - $$A_2$$ = 将被 5 除后余 1 的数字按给出顺序进行交错求和，即计算 $$n_1-n_2+n_3-n_4\cdots$$；
// - $$A_3$$ = 被 5 除后余 2 的数字的个数；
// - $$A_4$$ = 被 5 除后余 3 的数字的平均数，精确到小数点后 1 位；
// - $$A_5$$ = 被 5 除后余 4 的数字中最大数字。
// 
// ### 输入格式：
// 
// 每个输入包含 1 个测试用例。每个测试用例先给出一个不超过 1000 的正整数 $$N$$，随后给出 $$N$$ 个不超过 1000 的待分类的正整数。数字间以空格分隔。
// 
// ### 输出格式：
// 
// 对给定的 $$N$$ 个正整数，按题目要求计算 $$A_1$$~$$A_5$$ 并在一行中顺序输出。数字间以空格分隔，但行末不得有多余空格。
// 
// 若其中某一类数字不存在，则在相应位置输出 `N`。
// 
// ### 输入样例 1：
// ```in
// 13 1 2 3 4 5 6 7 8 9 10 20 16 18
// ```
// 
// ### 输出样例 1：
// ```out
// 30 11 2 9.7 9
// ```
// 
// ### 输入样例 2：
// ```in
// 8 1 2 4 5 6 7 9 16
// ```
// 
// ### 输出样例 2：
// ```out
// N 11 2 N 9
// ```

#include <iostream>
#include <iomanip>

using namespace std;

int main() {
    int N, n;
    bool A1 = false, A2 = false, A3 = false, A4 = false, A5 = false;
    int A1_sum = 0, A2_sum = 0, A2_sign = 1, A3_count = 0, A4_count = 0, A5_max = -1;
    float A4_sum = 0;

    cin >> N;
    for (int i = 0; i < N; ++i) {
        cin >> n;
        // A1
        if (n % 5 == 0 && n % 2 == 0) {
            A1_sum += n;
            A1 = true;
        }
        // A2
        if (n % 5 == 1) {
            A2_sum += (A2_sign * n);
            A2_sign = -A2_sign;
            A2 = true;
        }
        // A3
        if (n % 5 == 2) {
            ++A3_count;
            A3 = true;
        }
        // A4
        if (n % 5 == 3) {
            A4_sum += n;
            ++A4_count;
            A4 = true;
        }
        // A5
        if (n % 5 == 4 && n > A5_max) {
            A5_max = n;
            A5 = true;
        }
    }

    !A1 ? cout << "N " : cout << A1_sum << " ";
    !A2 ? cout << "N " : cout << A2_sum << " ";
    !A3 ? cout << "N " : cout << A3_count << " ";
    !A4 ? cout << "N " : cout << fixed << setprecision(1) << A4_sum / A4_count<< " ";
    !A5 ? cout << "N" : cout << A5_max;
    return 0;
}
            