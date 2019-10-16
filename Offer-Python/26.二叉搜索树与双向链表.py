## 题目描述
# 输入一棵二叉搜索树，将该二叉搜索树转换成一个排序的双向链表。
# 要求不能创建任何新的结点，只能调整树中结点指针的指向。

# -*- coding:utf-8 -*-
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def __init__(self):
        self.LDR_nodes = []

    def Convert(self, pRootOfTree):
        # write code here
        if not pRootOfTree:
            return None

        self.ConvertLDR(pRootOfTree)

        for i in range(1, len(self.LDR_nodes)-1):
            self.LDR_nodes[i].left = self.LDR_nodes[i-1]
            self.LDR_nodes[i].right = self.LDR_nodes[i+1]
        if len(self.LDR_nodes)>1:
            self.LDR_nodes[0].right = self.LDR_nodes[1]
            self.LDR_nodes[-1].left = self.LDR_nodes[-2]

        return self.LDR_nodes[0]

    def ConvertLDR(self, pRoot):
        if pRoot:
            self.ConvertLDR(pRoot.left)
            self.LDR_nodes.append(pRoot)
            self.ConvertLDR(pRoot.right)


if __name__ == "__main__":
    head = TreeNode(1)
    left = TreeNode(2)
    right = TreeNode(3)
    head.left = left
    head.right = right

    s = Solution()
    s.Convert(head)
    for node in s.LDR_nodes:
        print(node.val)