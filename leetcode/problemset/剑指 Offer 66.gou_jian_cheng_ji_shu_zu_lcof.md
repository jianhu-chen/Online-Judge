# 剑指 Offer 66. 构建乘积数组

[打开力扣](https://leetcode.cn/problems/gou-jian-cheng-ji-shu-zu-lcof) [我的代码](剑指 Offer 66.gou_jian_cheng_ji_shu_zu_lcof.py)

给定一个数组 <code>A[0,1,…,n-1]</code>，请构建一个数组 <code>B[0,1,…,n-1]</code>，其中 <code>B[i]</code> 的值是数组 <code>A</code> 中除了下标 <code>i</code> 以外的元素的积, 即 <code>B[i]=A[0]×A[1]×…×A[i-1]×A[i+1]×…×A[n-1]</code>。不能使用除法。

 

<strong>示例:</strong>

<pre>
<strong>输入:</strong> [1,2,3,4,5]
<strong>输出:</strong> [120,60,40,30,24]</pre>

 

<strong>提示：</strong>

<ul>
	<li>所有元素乘积之和不会溢出 32 位整数</li>
	<li><code>a.length <= 100000</code></li>
</ul>
