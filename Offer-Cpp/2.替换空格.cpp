//
// Created by 陈建虎 on 2019-10-29.
//
// 题目描述
// 请实现一个函数，将一个字符串中的每个空格替换成“%20”。
// 例如，当字符串为We Are Happy.则经过替换之后的字符串为We%20Are%20Happy。

#include <iostream>
#include <cstring>

using namespace std;

class Solution {
public:
    void replaceSpace(char *str, int length) {
        if (str == nullptr || length < 0) {
            return;
        }

        int count = 0;
        for (int i = 0; i < length; ++i) {
            if (str[i] == ' ') {
                ++count;
            }
        }

        for (int i = length - 1; i >= 0; --i) {
            if (str[i] == ' ') {
                --count;
//                strcpy(&str[i + count * 2], "%20");
                str[i + count * 2] = '%';
                str[i + count * 2 + 1] = '2';
                str[i + count * 2 + 2] = '0';
            } else {
                str[i + count * 2] = str[i];
            }
        }

    }
};


int main() {
    char str[100] = "we are happy!";
    cout << str << endl;
    Solution sol = Solution();
    sol.replaceSpace(str, strlen(str));
    cout << str << endl;
    return 0;
}