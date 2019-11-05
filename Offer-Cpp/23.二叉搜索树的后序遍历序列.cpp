//
// Created by 陈建虎 on 2019-11-05.
//
// 题目描述
// 输入一个整数数组，判断该数组是不是某二叉搜索树的后序遍历的结果。
// 如果是则输出Yes,否则输出No。假设输入的数组的任意两个数字都互不相同。

#include <iostream>
#include <vector>

using namespace std;

class Solution {
public:
    bool VerifySquenceOfBST(vector<int> sequence) {
        if (sequence.empty()) {
            return false;
        }
        if (sequence.size() == 1) {
            return true;
        }
        int root = sequence.back();
        auto left = sequence.begin();
        while (*(left++) < root);
        for (auto it = left; it != sequence.end(); ++it) {
            if (*it < root) {
                return false;
            }
        }
        return VerifySquenceOfBST(vector<int>(sequence.begin(), --left)) ||
               VerifySquenceOfBST(vector<int>(left, --sequence.end()));
    }
};


int main() {
    vector<int> v;
    for (int i = 0; i < 10; i++) {
        v.push_back(i);
    }

    for (int i = 0; i < vector<int>(v.begin(), -- --v.end()).size(); i++) {
        cout << vector<int>(v.begin(), -- --v.end())[i] << " ";
    }
//    cout << *(--v.end());
    return 0;
}