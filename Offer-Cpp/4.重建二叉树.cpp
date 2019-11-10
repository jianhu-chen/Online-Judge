//
// Created by jhchen on 2019/11/1.
//
// 题目描述
// 输入某二叉树的前序遍历和中序遍历的结果，请重建出该二叉树。
// 假设输入的前序遍历和中序遍历的结果中都不含重复的数字。
// 例如输入前序遍历序列{1,2,4,7,3,5,6,8}和中序遍历
// 序列{4,7,2,1,5,3,8,6}，则重建二叉树并返回。

#include <iostream>
#include <vector>

using namespace std;

/**
 * Definition for binary tree
**/
struct TreeNode {
    int val;
    TreeNode *left;
    TreeNode *right;

    TreeNode(int x) : val(x), left(NULL), right(NULL) {}
};

class Solution {
public:
    TreeNode *reConstructBinaryTree(vector<int> pre, vector<int> vin) {
        if (pre.size() == 0 || vin.size() == 0 || pre.size() != vin.size()) {
            return NULL;
        }
        TreeNode *root = new TreeNode(pre[0]);
        int index = 0;
        for (int i = 0; i < vin.size(); ++i) {
            if (pre[0] == vin[i]) {
                index = i;
                break;
            }
        }
        vector<int> subPreLeft;
        for (int i = 1; i <= index; ++i) {
            subPreLeft.push_back(pre[i]);
        }
        vector<int> subPreRight;
        for (int i = index + 1; i < pre.size(); ++i) {
            subPreRight.push_back(pre[i]);
        }
        vector<int> subVinLeft;
        for (int i = 0; i < index; ++i) {
            subVinLeft.push_back(vin[i]);
        }
        vector<int> subVinRight;
        for (int i = index + 1; i < vin.size(); ++i) {
            subVinRight.push_back(vin[i]);
        }

        root->left = reConstructBinaryTree(subPreLeft, subVinLeft);
        root->right = reConstructBinaryTree(subPreRight, subVinRight);

        return root;
    }
};