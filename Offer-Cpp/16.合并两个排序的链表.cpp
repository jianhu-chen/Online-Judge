//
// Created by 陈建虎 on 2019-11-04.
//
//题目描述
//输入两个单调递增的链表，输出两个链表合成后的链表，当然我们需要合成后的链表满足单调不减规则。

#include <iostream>

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
    ListNode *Merge(ListNode *pHead1, ListNode *pHead2) {
        ListNode *pHead = new ListNode(0);
        ListNode *pRoot = pHead;
        while (pHead1 && pHead2) {
            ListNode *newNode = new ListNode(0);
            if (pHead1->val < pHead2->val) {
                newNode->val = pHead1->val;
                pHead1 = pHead1->next;
            } else {
                newNode->val = pHead2->val;
                pHead2 = pHead2->next;
            }
            pHead->next = newNode;
            pHead = pHead->next;
        }

        while (pHead1) {
            ListNode *newNode = new ListNode(pHead1->val);
            pHead->next = newNode;
            pHead = pHead->next;
            pHead1 = pHead1->next;
        }

        while (pHead2) {
            ListNode *newNode = new ListNode(pHead2->val);
            pHead->next = newNode;
            pHead = pHead->next;
            pHead2 = pHead2->next;
        }

        return pRoot->next;
    }
};