# 剑指 Offer 55 - II. 平衡二叉树

[打开力扣](https://leetcode.cn/problems/ping-heng-er-cha-shu-lcof) [我的代码](剑指 Offer 55 - II.ping_heng_er_cha_shu_lcof.py)

输入一棵二叉树的根节点，判断该树是不是平衡二叉树。如果某二叉树中任意节点的左右子树的深度相差不超过1，那么它就是一棵平衡二叉树。

 

<strong>示例 1:</strong>

给定二叉树 <code>[3,9,20,null,null,15,7]</code>

<pre>
    3
   / \
  9  20
    /  \
   15   7</pre>

返回 <code>true</code> 。<br />
<br />
<strong>示例 2:</strong>

给定二叉树 <code>[1,2,2,3,3,null,null,4,4]</code>

<pre>
       1
      / \
     2   2
    / \
   3   3
  / \
 4   4
</pre>

返回 <code>false</code> 。

 

<strong>限制：</strong>

<ul>
	<li><code>0 <= 树的结点个数 <= 10000</code></li>
</ul>

注意：本题与主站 110 题相同：<a href="https://leetcode-cn.com/problems/balanced-binary-tree/">https://leetcode-cn.com/problems/balanced-binary-tree/</a>
