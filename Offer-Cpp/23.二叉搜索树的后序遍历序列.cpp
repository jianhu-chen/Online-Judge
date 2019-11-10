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
    bool first = true;

    bool VerifySquenceOfBST(vector<int> sequence) {
        if (sequence.empty() && first) {
            return false;
        }
        first = false;
        if (sequence.size() <= 2) {
            return true;
        }
        int root = sequence.back();
        auto mid = sequence.begin();
        while (*(mid++) < root);
        for (auto it = mid; it != sequence.end(); ++it) {
            if (*it < root) {
                return false;
            }
        }
        vector<int> left(sequence.begin(), --mid);
        vector<int> right(mid, --sequence.end());
        return VerifySquenceOfBST(left) &&
               VerifySquenceOfBST(right);
    }
};


int main() {
    vector<int> v;
    v.push_back(1);
    v.push_back(2);
    v.push_back(3);
    v.push_back(4);
    v.push_back(5);

//    for (int i = 0; i < v.size(); i++) {
//        cout << v[i] << " ";
//    }

    Solution s;
    bool rst = s.VerifySquenceOfBST(v);
    cout << rst;
    return 0;
}