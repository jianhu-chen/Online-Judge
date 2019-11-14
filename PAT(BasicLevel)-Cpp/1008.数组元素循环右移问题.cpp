//
// Created by jhchen<jianhuchen@163.com> on 2019-11-12 15:03:33.
//
// 题目链接: https://pintia.cn/problem-sets/994805260223102976/problems/994805316250615808
// 题目描述: 一个数组$$A$$中存有$$N$$（$$>0$$）个整数，在不允许使用另外数组的前提下，将每个整数循环向右移$$M$$（$$\ge 0$$）个位置，即将$$A$$中的数据由（$$A_0 A_1 \cdots A_{N-1}$$）变换为（$$A_{N-M} \cdots A_{N-1} A_0 A_1 \cdots A_{N-M-1}$$）（最后$$M$$个数循环移至最前面的$$M$$个位置）。如果需要考虑程序移动数据的次数尽量少，要如何设计移动的方法？
// 
// ### 输入格式:
// 
// 每个输入包含一个测试用例，第1行输入$$N$$（$$1\le N \le 100$$）和$$M$$（$$\ge 0$$）；第2行输入$$N$$个整数，之间用空格分隔。
// 
// ### 输出格式:
// 
// 在一行中输出循环右移$$M$$位以后的整数序列，之间用空格分隔，序列结尾不能有多余空格。
// 
// ### 输入样例:
// ```in
// 6 2
// 1 2 3 4 5 6
// ```
// 
// ### 输出样例:
// ```out
// 5 6 1 2 3 4
// 
#include <iostream>
#include <queue>

using namespace std;

int main() {
    int N, M, n;
    queue<int> que;
    cin >> N >> M;
    for (int i = 0; i < N; ++i) {
        cin >> n;
        que.push(n);
    }

    for (int i = 0; i < N - M % N; ++i) {
        que.push(que.front());
        que.pop();
    }

    while (!que.empty()) {
        cout << que.front();
        if (que.size() != 1) {
            cout << " ";
        }
        que.pop();
    }
    return 0;
}
            