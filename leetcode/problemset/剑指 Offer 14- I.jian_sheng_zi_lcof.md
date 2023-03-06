# 剑指 Offer 14- I. 剪绳子

[打开力扣](https://leetcode.cn/problems/jian-sheng-zi-lcof) [我的代码](剑指 Offer 14- I.jian_sheng_zi_lcof.py)

给你一根长度为 <code>n</code> 的绳子，请把绳子剪成整数长度的 <code>m</code> 段（m、n都是整数，n>1并且m>1），每段绳子的长度记为 <code>k[0],k[1]...k[m-1]</code> 。请问 <code>k[0]*k[1]*...*k[m-1]</code> 可能的最大乘积是多少？例如，当绳子的长度是8时，我们把它剪成长度分别为2、3、3的三段，此时得到的最大乘积是18。

<strong>示例 1：</strong>

<pre><strong>输入: </strong>2
<strong>输出: </strong>1
<strong>解释: </strong>2 = 1 + 1, 1 &times; 1 = 1</pre>

<strong>示例2:</strong>

<pre><strong>输入: </strong>10
<strong>输出: </strong>36
<strong>解释: </strong>10 = 3 + 3 + 4, 3 &times;3 &times;4 = 36</pre>

<strong>提示：</strong>

<ul>
	<li><code>2 <= n <= 58</code></li>
</ul>

注意：本题与主站 343 题相同：<a href="https://leetcode-cn.com/problems/integer-break/">https://leetcode-cn.com/problems/integer-break/</a>
