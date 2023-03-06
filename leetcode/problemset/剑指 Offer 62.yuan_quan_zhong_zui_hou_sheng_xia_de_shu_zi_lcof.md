# 剑指 Offer 62. 圆圈中最后剩下的数字

[打开力扣](https://leetcode.cn/problems/yuan-quan-zhong-zui-hou-sheng-xia-de-shu-zi-lcof) [我的代码](剑指 Offer 62.yuan_quan_zhong_zui_hou_sheng_xia_de_shu_zi_lcof.py)

0,1,···,n-1这n个数字排成一个圆圈，从数字0开始，每次从这个圆圈里删除第m个数字（删除后从下一个数字开始计数）。求出这个圆圈里剩下的最后一个数字。

例如，0、1、2、3、4这5个数字组成一个圆圈，从数字0开始每次删除第3个数字，则删除的前4个数字依次是2、0、4、1，因此最后剩下的数字是3。

 

<strong>示例 1：</strong>

<pre>
<strong>输入:</strong> n = 5, m = 3
<strong>输出: </strong>3
</pre>

<strong>示例 2：</strong>

<pre>
<strong>输入:</strong> n = 10, m = 17
<strong>输出: </strong>2
</pre>

 

<strong>限制：</strong>

<ul>
	<li><code>1 <= n <= 10^5</code></li>
	<li><code>1 <= m <= 10^6</code></li>
</ul>
