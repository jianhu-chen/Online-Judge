//
// Created by 陈建虎 on 2019-11-05.
//
// 题目描述
// 输入一个字符串,按字典序打印出该字符串中字符的所有排列。
// 例如输入字符串abc,则打印出由字符a,b,c所能排列出来的所有字符串abc,acb,bac,bca,cab和cba。
// 输入描述:
// 输入一个字符串,长度不超过9(可能有字符重复),字符只包括大小写字母。

#include <iostream>
#include <string>
#include <vector>
#include <algorithm>
#include<functional>

using namespace std;

class Solution {
public:
    vector <string> Permutation(string str) {
        if (str.length() == 0) {
            return vector<string>();
        }
        if (str.length() == 1) {
            return vector<string>(1, str);
        }

        vector <string> result;
        string s = string(1, str[0]);
        vector <string> subStrVec = Permutation(str.substr(1, str.length() - 1));
        for (int i = 0; i < subStrVec.size(); i++) {
            for (int j = 0; j < subStrVec[i].length() + 1; j++) {
                string substring = subStrVec[i];
                result.push_back(substring.insert(j, s));
            }
        }
        sort(result.begin(), result.end(), less<string>());
        auto it = unique(result.begin(), result.end());
        result.erase(it, result.end());
        return result;
    }
};

int main() {
    string str = "aa";
    Solution solution = Solution();
    vector <string> v = solution.Permutation(str);
    for (int i = 0; i < v.size(); i++) {
        cout << v[i] << endl;
    }
    return 0;
}