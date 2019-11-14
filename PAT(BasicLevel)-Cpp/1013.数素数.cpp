//
// Created by jhchen<jianhuchen@163.com> on 2019-11-12 15:03:35.
//
// 题目链接: https://pintia.cn/problem-sets/994805260223102976/problems/994805309963354112
// 题目描述: 令 $$P_i$$ 表示第 $$i$$ 个素数。现任给两个正整数 $$M \le N \le 10^4$$，请输出 $$P_M$$ 到 $$P_N$$ 的所有素数。
// 
// ### 输入格式：
// 
// 输入在一行中给出 $$M$$ 和 $$N$$，其间以空格分隔。
// 
// ### 输出格式：
// 
// 输出从 $$P_M$$ 到 $$P_N$$ 的所有素数，每 10 个数字占 1 行，其间以空格分隔，但行末不得有多余空格。
// 
// ### 输入样例：
// ```in
// 5 27
// ```
// 
// ### 输出样例：
// ```out
// 11 13 17 19 23 29 31 37 41 43
// 47 53 59 61 67 71 73 79 83 89
// 97 101 103
// ```

#include <iostream>
#include <vector>
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
    int M, N, n = 2, newLine = 1;
    vector<int> sushu;
    cin >> M >> N;
    while (sushu.size() < N) {
        if (isSushu(n)) {
            sushu.push_back(n);
        }
        ++n;
    }
    for (int i = M - 1; i <= N - 1; ++i) {
        cout << sushu[i];
        if (newLine % 10 == 0) {
            cout << endl;
        } else if (i != N - 1) {
            cout << " ";
        }
        ++newLine;
    }
    return 0;
}
            