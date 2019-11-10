//
// Created by 陈建虎 on 2019-11-04.
//
//题目描述
//输入一个链表，输出该链表中倒数第k个结点。

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
    ListNode *FindKthToTail(ListNode *pListHead, unsigned int k) {
        if (pListHead == NULL) {
            return NULL;
        }
        if (k <= 0) {
            return NULL;
        }
        vector < ListNode * > nodes;
        ListNode *pHead = pListHead;
        while (pHead) {
            nodes.push_back(pHead);
            pHead = pHead->next;
        }

        if (k > nodes.size()) {
            return NULL;
        }
        return nodes[nodes.size() - k];
    }
};