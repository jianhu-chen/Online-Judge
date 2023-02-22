# 剑指 Offer 34. 二叉树中和为某一值的路径

[打开力扣](https://leetcode.cn/problems/er-cha-shu-zhong-he-wei-mou-yi-zhi-de-lu-jing-lcof) [我的代码](剑指 Offer 34.er_cha_shu_zhong_he_wei_mou_yi_zhi_de_lu_jing_lcof.py)

给你二叉树的根节点 <code>root</code> 和一个整数目标和 <code>targetSum</code> ，找出所有 <strong>从根节点到叶子节点</strong> 路径总和等于给定目标和的路径。

<strong>叶子节点</strong> 是指没有子节点的节点。



<strong>示例 1：</strong>

<img alt="" src="https://assets.leetcode.com/uploads/2021/01/18/pathsumii1.jpg" />

<pre>
<strong>输入：</strong>root = [5,4,8,11,null,13,4,7,2,null,null,5,1], targetSum = 22
<strong>输出：</strong>[[5,4,11,2],[5,8,4,5]]
</pre>

<strong>示例 2：</strong>

<img alt="" src="https://assets.leetcode.com/uploads/2021/01/18/pathsum2.jpg" />

<pre>
<strong>输入：</strong>root = [1,2,3], targetSum = 5
<strong>输出：</strong>[]
</pre>

<strong>示例 3：</strong>

<pre>
<strong>输入：</strong>root = [1,2], targetSum = 0
<strong>输出：</strong>[]
</pre>



<strong>提示：</strong>

<ul>
	<li>树中节点总数在范围 <code>[0, 5000]</code> 内</li>
	<li><code>-1000 <= Node.val <= 1000</code></li>
	<li><code>-1000 <= targetSum <= 1000</code></li>
</ul>

注意：本题与主站 113题相同：<a href="https://leetcode-cn.com/problems/path-sum-ii/">https://leetcode-cn.com/problems/path-sum-ii/</a>
