//
// Created by 陈建虎 on 2019-11-05.
//
//题目描述
//输入一个复杂链表（每个节点中有节点值，以及两个指针，一个指向下一个节点，
//另一个特殊指针指向任意一个节点），返回结果为复制后复杂链表的head。
//（注意，输出结果中请不要返回参数中的节点引用，否则判题程序会直接返回空）

#include <iostream>

using namespace std;

struct RandomListNode {
    int label;
    struct RandomListNode *next, *random;

    RandomListNode(int x) :
            label(x), next(NULL), random(NULL) {
    }
};

class Solution {
public:
    RandomListNode *Clone(RandomListNode *pHead) {
        if (pHead == NULL) {
            return NULL;
        }
        RandomListNode *currNode = pHead;
        while (currNode) {
            RandomListNode *node = new RandomListNode(currNode->label);
            node->next = currNode->next;
            currNode->next = node;
            currNode = node->next;
        }

        currNode = pHead;
        while (currNode) {
            if (currNode->random) {
                currNode->next->random = currNode->random->next;
            }
            currNode = currNode->next->next;
        }

        RandomListNode *cloneHead = pHead->next;
        RandomListNode *tmp;
        currNode = pHead;
        while (currNode->next) {
            tmp = currNode->next;
            currNode->next = tmp->next;
            currNode = tmp;
        }
        return cloneHead;
    }
};