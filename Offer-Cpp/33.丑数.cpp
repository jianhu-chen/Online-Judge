//
// Created by 陈建虎 on 2019-11-02.
//

#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

class Solution {
public:
    int GetUglyNumber_Solution(int index) {
        if (index <= 0) {
            return 0;
        }
        if (index == 1) {
            return 1;
        }
        vector<long> uglyList;
        uglyList.push_back(1);
        int index_2 = 0;
        int index_3 = 0;
        int index_5 = 0;
        for (int i = 0; i < index - 1; ++i) {
            int newUgly = min(uglyList[index_2] * 2, min(uglyList[index_3] * 3, uglyList[index_5] * 5));
            uglyList.push_back(newUgly);
            if (newUgly % 2 == 0) {
                ++index_2;
            }
            if (newUgly % 3 == 0) {
                ++index_3;
            }
            if (newUgly % 5 == 0) {
                ++index_5;
            }
        }
        return uglyList.back();
    }
};

int main() {
    Solution s = Solution();
    s.GetUglyNumber_Solution(9999);
    return 0;
}