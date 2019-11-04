//
// Created by 陈建虎 on 2019-11-04.
//
// 题目描述
// 输入一个链表，反转链表后，输出新链表的表头。

#include <iostream>
#include <vector>

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
    ListNode *ReverseList(ListNode *pHead) {
        if (pHead == NULL) {
            return NULL;
        }

        vector<ListNode *> nodes;
        while (pHead) {
            nodes.push_back(pHead);
            pHead = pHead->next;
        }

        for (int i = nodes.size() - 1; i > 0; --i) {
            nodes[i]->next = nodes[i - 1];
        }
        nodes[0]->next = NULL;

        return nodes.back();
    }
};