//
// Created by 陈建虎 on 2019-11-05.
//
//题目描述
//从上往下打印出二叉树的每个节点，同层节点从左至右打印。

#include <iostream>
#include <vector>
#include <queue>

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
    vector<int> PrintFromTopToBottom(TreeNode *root) {
        vector<int> rst;
        if (root == nullptr) {
            return rst;
        }
        queue < TreeNode * > que;
        que.push(root);
        while (!que.empty()) {
            TreeNode *head = que.front();
            rst.push_back(head->val);
            if (head->left) {
                que.push(head->left);
            }
            if (head->right) {
                que.push(head->right);
            }
            que.pop();
        }

        return rst;
    }
};