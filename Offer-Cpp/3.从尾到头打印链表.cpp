//
// Created by jhchen on 2019/10/30.
//
// 题目描述
// 输入一个链表，按链表从尾到头的顺序返回一个ArrayList。

#include <iostream>
#include <vector>
#include <stack>

using namespace std;

struct ListNode {
    int val;
    struct ListNode *next;

    ListNode(int x) :
            val(x), next(NULL) {
    }
};

class Solution {
public:
    vector<int> printListFromTailToHead(ListNode *head) {
        vector<int> ret;
        stack<int> tempStack;

        if (head == NULL) {
            return ret;
        }

        ListNode *pHead = head;
        while (pHead) {
            tempStack.push(pHead->val);
            pHead = pHead->next;
        }

        while (!tempStack.empty()) {
            ret.push_back(tempStack.top());
            tempStack.pop();
        }

        return ret;
    }
};


int main() {

    return 0;
}
