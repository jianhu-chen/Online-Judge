# 剑指 Offer 28. 对称的二叉树

[打开力扣](https://leetcode.cn/problems/dui-cheng-de-er-cha-shu-lcof) [我的代码](剑指 Offer 28.dui_cheng_de_er_cha_shu_lcof.py)

请实现一个函数，用来判断一棵二叉树是不是对称的。如果一棵二叉树和它的镜像一样，那么它是对称的。

例如，二叉树[1,2,2,3,4,4,3] 是对称的。

<code>  1<br>
 / \<br>
 2  2<br>
/ \ / \<br>
3 4 4 3</code><br>
但是下面这个[1,2,2,null,3,null,3] 则不是镜像对称的:

<code>  1<br>
 / \<br>
 2  2<br>
 \  \<br>
 3  3</code>



<strong>示例 1：</strong>

<pre><strong>输入：</strong>root = [1,2,2,3,4,4,3]
<strong>输出：</strong>true
</pre>

<strong>示例 2：</strong>

<pre><strong>输入：</strong>root = [1,2,2,null,3,null,3]
<strong>输出：</strong>false</pre>



<strong>限制：</strong>

<code>0 <= 节点个数 <= 1000</code>

注意：本题与主站 101 题相同：<a href="https://leetcode-cn.com/problems/symmetric-tree/">https://leetcode-cn.com/problems/symmetric-tree/</a>
