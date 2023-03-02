# 剑指 Offer 07. 重建二叉树

[打开力扣](https://leetcode.cn/problems/zhong-jian-er-cha-shu-lcof) [我的代码](剑指 Offer 07.zhong_jian_er_cha_shu_lcof.py)

输入某二叉树的前序遍历和中序遍历的结果，请构建该二叉树并返回其根节点。

假设输入的前序遍历和中序遍历的结果中都不含重复的数字。

 

<strong>示例 1:</strong>
<img alt="" src="https://assets.leetcode.com/uploads/2021/02/19/tree.jpg" />
<pre>
<strong>Input:</strong> preorder = [3,9,20,15,7], inorder = [9,3,15,20,7]
<strong>Output:</strong> [3,9,20,null,null,15,7]
</pre>

<strong>示例 2:</strong>

<pre>
<strong>Input:</strong> preorder = [-1], inorder = [-1]
<strong>Output:</strong> [-1]
</pre>

 

<strong>限制：</strong>

<code>0 <= 节点个数 <= 5000</code>

 

<strong>注意</strong>：本题与主站 105 题重复：<a href="https://leetcode-cn.com/problems/construct-binary-tree-from-preorder-and-inorder-traversal/">https://leetcode-cn.com/problems/construct-binary-tree-from-preorder-and-inorder-traversal/</a>
