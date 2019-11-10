//
// Created by 陈建虎 on 2019-10-29.
//
// 题目描述
// 在一个二维数组中（每个一维数组的长度相同），每一行都按照从左到右递增的顺序排序，
// 每一列都按照从上到下递增的顺序排序。请完成一个函数，输入这样的一个二维数组和一个整数，
// 判断数组中是否含有该整数。

#include <iostream>
#include <vector>

using namespace std;

class Solution {
public:
    bool Find(int target, vector <vector<int>> array) {
        for (vector < vector < int >> ::iterator it = array.begin(); it != array.end();
        it++) {
            for (vector<int>::iterator itit = it->begin(); itit != it->end(); itit++) {
                if (target == *itit) {
                    return true;
                }
            }
        }
        return false;
    }
};

void print(int val) {
    cout << val << "\t";
}

void vectorPrint(vector<int> v) {
    for_each(v.begin(), v.end(), print);
    cout << endl;
}

int main() {
    int target = 9999;
    vector <vector<int>> array;
    for (int i = 0; i < 5; i++) {
        vector<int> a;
        for (int j = 0; j < 5; j++) {
            a.push_back(i * 5 + j);
        }
        array.push_back(a);
    }

    for_each(array.begin(), array.end(), vectorPrint);

    Solution sol = Solution();
    bool ans = sol.Find(target, array);
    cout << ans << endl;
    return 0;
}