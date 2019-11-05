//
// Created by 陈建虎 on 2019-11-05.
//
//题目描述
//定义栈的数据结构，请在该类型中实现一个能够得到栈中所含最小元素的min函数（时间复杂度应为O（1））。
//
// 思路
// 增加一个辅助栈
// push时：如果A栈的压入比B栈压入大，B栈不压，小于等于，AB栈同时压入
// pop时：如果，AB栈顶元素不等，A出，B不出。

#include <iostream>
#include <stack>

using namespace std;

class Solution {
public:
    void push(int value) {
        st.push(value);
        if (stmin.empty()) {
            stmin.push(value);
        } else {
            if (value < stmin.top()) {
                stmin.push(value);
            }
        }
    }

    void pop() {
        if (st.top() == stmin.top()) {
            stmin.pop();
        }
        st.pop();
    }

    int top() {
        return st.top();
    }

    int min() {
        return stmin.top();
    }

private:
    stack<int> st;
    stack<int> stmin;
};