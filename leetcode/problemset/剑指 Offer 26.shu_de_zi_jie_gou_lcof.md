# 剑指 Offer 26. 树的子结构

[打开力扣](https://leetcode.cn/problems/shu-de-zi-jie-gou-lcof) [我的代码](剑指 Offer 26.shu_de_zi_jie_gou_lcof.py)

输入两棵二叉树A和B，判断B是不是A的子结构。(约定空树不是任意一个树的子结构)

B是A的子结构， 即 A中有出现和B相同的结构和节点值。

例如:<br>
给定的树 A:

<code>  3<br>
  / \<br>
 4  5<br>
 / \<br>
1  2</code><br>
给定的树 B：

<code> 4<br>
 /<br>
1</code><br>
返回 true，因为 B 与 A 的一个子树拥有相同的结构和节点值。

<strong>示例 1：</strong>

<pre><strong>输入：</strong>A = [1,2,3], B = [3,1]
<strong>输出：</strong>false
</pre>

<strong>示例 2：</strong>

<pre><strong>输入：</strong>A = [3,4,5,1,2], B = [4,1]
<strong>输出：</strong>true</pre>

<strong>限制：</strong>

<code>0 <= 节点个数 <= 10000</code>
