//
// Created by jhchen<jianhuchen@163.com> on 2019-11-12 15:03:37.
//
// 题目链接: https://pintia.cn/problem-sets/994805260223102976/problems/994805304020025344
// 题目描述: 大家应该都会玩“锤子剪刀布”的游戏：两人同时给出手势，胜负规则如图所示：
// 
// 
// ![FigCJB.jpg](~/724da598-b37f-4f1f-99b4-71459654ce3a.jpg)
// 
// 
// 现给出两人的交锋记录，请统计双方的胜、平、负次数，并且给出双方分别出什么手势的胜算最大。
// 
// ### 输入格式：
// 
// 输入第 1 行给出正整数 $$N$$（$$\le 10^5$$），即双方交锋的次数。随后 $$N$$ 行，每行给出一次交锋的信息，即甲、乙双方同时给出的的手势。`C` 代表“锤子”、`J` 代表“剪刀”、`B` 代表“布”，第 1 个字母代表甲方，第 2 个代表乙方，中间有 1 个空格。
// 
// ### 输出格式：
// 
// 输出第 1、2 行分别给出甲、乙的胜、平、负次数，数字间以 1 个空格分隔。第 3 行给出两个字母，分别代表甲、乙获胜次数最多的手势，中间有 1 个空格。如果解不唯一，则输出按字母序最小的解。
// 
// ### 输入样例：
// ```in
// 10
// C J
// J B
// C B
// B B
// B C
// C C
// C B
// J B
// B C
// J J
// ```
// 
// ### 输出样例：
// ```out
// 5 3 2
// 2 3 5
// B B
// ```

#include <iostream>
#include <map>
#include <algorithm>

using namespace std;

int isWin(char a, char b) {
    if (a == 'B') {
        if (b == 'B') {
            return 0;
        } else if (b == 'C') {
            return 1;
        } else {
            return -1;
        }
    } else if (a == 'C') {
        if (b == 'B') {
            return -1;
        } else if (b == 'C') {
            return 0;
        } else {
            return 1;
        }
    } else {
        if (b == 'B') {
            return 1;
        } else if (b == 'C') {
            return -1;
        } else {
            return 0;
        }
    }
}

char getWinGesture(int *winCount) {
    int maxCount = max(winCount[0], max(winCount[1], winCount[2]));
    if (winCount[0] == maxCount) {
        return 'B';
    } else if (winCount[1] == maxCount) {
        return 'C';
    } else {
        return 'J';
    }
}

int main() {
    int N, winSummary[2][3] = {0}, winCount[2][3]={0};
    char jia, yi;
    map<char, int> convert;
    convert.insert(make_pair('B', 0));
    convert.insert(make_pair('C', 1));
    convert.insert(make_pair('J', 2));

    cin >> N;
    for (int i = 0; i < N; ++i) {
        cin >> jia >> yi;
        if (isWin(jia, yi) == 1) {
            ++winCount[0][convert[jia]];
            ++winSummary[0][0];
            ++winSummary[1][2];
        } else if (isWin(jia, yi) == 0) {
            ++winSummary[0][1];
            ++winSummary[1][1];
        } else {
            ++winCount[1][convert[yi]];
            ++winSummary[0][2];
            ++winSummary[1][0];
        }
    }

    cout << winSummary[0][0] << " " << winSummary[0][1] << " " << winSummary[0][2] << endl;
    cout << winSummary[1][0] << " " << winSummary[1][1] << " " << winSummary[1][2] << endl;;
    cout << getWinGesture(winCount[0]) << " " << getWinGesture(winCount[1]);
    return 0;
}
            