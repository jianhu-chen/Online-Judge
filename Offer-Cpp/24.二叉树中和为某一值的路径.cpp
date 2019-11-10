//
// Created by 陈建虎 on 2019-11-05.
//
//题目描述
//输入一颗二叉树的跟节点和一个整数，打印出二叉树中结点值的和为输入整数的所有路径。
//路径定义为从树的根结点开始往下一直到叶结点所经过的结点形成一条路径。
//(注意: 在返回值的list中，数组长度大的数组靠前)

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
    vector<vector<int>> FindPath(TreeNode *root, int expectNumber) {
        if (root == NULL) {
            return vector<vector<int>>();
        }
        if (root && root->left == NULL && root->right == NULL and root->val == expectNumber) {
            return vector<vector<int>>(1, vector<int>(1, root->val));
        }
        vector<int> result;
        vector<vector<int>> left = FindPath(root->left, expectNumber-root->val);
        vector<vector<int>> right = FindPath(root->right, expectNumber-root->val);
        for (auto it =left.begin(); it!=left.end(); it++){
            result.push_back();
        }
        for (auto it =right.begin(); it!=right.end(); it++){

        }
    }
};