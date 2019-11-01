//
// Created by jhchen on 2019/11/1.
//
// 题目描述
// 用两个栈来实现一个队列，完成队列的Push和Pop操作。 队列中的元素为int类型。

#include <iostream>
#include <stack>

using namespace std;


class Solution {
public:
    void push(int node) {
        stack1.push(node);
    }

    int pop() {
        if (!stack2.empty()) {
            int val = stack2.top();
            stack2.pop();
            return val;
        } else {
            while (!stack1.empty()) {
                stack2.push(stack1.top());
                stack1.pop();
            }
            int val = stack2.top();
            stack2.pop();
            return val;
        }
    }

private:
    stack<int> stack1;
    stack<int> stack2;
};