# 剑指 Offer 10- I. 斐波那契数列

[打开力扣](https://leetcode.cn/problems/fei-bo-na-qi-shu-lie-lcof) [我的代码](剑指 Offer 10- I.fei_bo_na_qi_shu_lie_lcof.py)

写一个函数，输入 <code>n</code> ，求斐波那契（Fibonacci）数列的第 <code>n</code> 项（即 <code>F(N)</code>）。斐波那契数列的定义如下：

<pre>
F(0) = 0,   F(1) = 1
F(N) = F(N - 1) + F(N - 2), 其中 N > 1.</pre>

斐波那契数列由 0 和 1 开始，之后的斐波那契数就是由之前的两数相加而得出。

答案需要取模 1e9+7（1000000007），如计算初始结果为：1000000008，请返回 1。

 

<strong>示例 1：</strong>

<pre>
<strong>输入：</strong>n = 2
<strong>输出：</strong>1
</pre>

<strong>示例 2：</strong>

<pre>
<strong>输入：</strong>n = 5
<strong>输出：</strong>5
</pre>

 

<strong>提示：</strong>

<ul>
	<li><code>0 <= n <= 100</code></li>
</ul>
