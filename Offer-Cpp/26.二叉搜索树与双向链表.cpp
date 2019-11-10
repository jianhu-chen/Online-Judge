//
// Created by 陈建虎 on 2019-11-05.
//
//题目描述
//输入一棵二叉搜索树，将该二叉搜索树转换成一个排序的双向链表。要求不能创建任何新的结点，只能调整树中结点指针的指向。

#include <iostream>
#include <vector>

using namespace std;


struct TreeNode {
    int val;
    struct TreeNode *left;
    struct TreeNode *right;

    TreeNode(int x) :
            val(x), left(NULL), right(NULL) {
    }
};

class Solution {
public:
    TreeNode *Convert(TreeNode *pRootOfTree) {
        if (pRootOfTree == NULL) {
            return NULL;
        }
        ldr(pRootOfTree);
        for (int i = 0; i < ldrVector.size(); i++) {
            if (i == 0) {
                ldrVector[i]->left = NULL;
            } else {
                ldrVector[i]->left = ldrVector[i - 1];
            }
            if (i == ldrVector.size() - 1) {
                ldrVector[i]->right = NULL;
            } else {
                ldrVector[i]->right = ldrVector[i + 1];
            }
        }
        ldrVector.front()->left = NULL;
        ldrVector.back()->right = NULL;

        return ldrVector.front();
    }

    void ldr(TreeNode *pRootOfTree) {
        if (pRootOfTree != NULL) {
            ldr(pRootOfTree->left);
            ldrVector.push_back(pRootOfTree);
            ldr(pRootOfTree->right);
        }
    }

private:
    vector<TreeNode *> ldrVector;
};