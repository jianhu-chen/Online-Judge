# 剑指 Offer 11. 旋转数组的最小数字

[打开力扣](https://leetcode.cn/problems/xuan-zhuan-shu-zu-de-zui-xiao-shu-zi-lcof) [我的代码](剑指 Offer 11.xuan_zhuan_shu_zu_de_zui_xiao_shu_zi_lcof.py)

把一个数组最开始的若干个元素搬到数组的末尾，我们称之为数组的旋转。

给你一个可能存在<strong>重复</strong>元素值的数组<code>numbers</code>，它原来是一个升序排列的数组，并按上述情形进行了一次旋转。请返回旋转数组的<strong>最小元素</strong>。例如，数组<code>[3,4,5,1,2]</code> 为 <code>[1,2,3,4,5]</code> 的一次旋转，该数组的最小值为 1。

注意，数组 <code>[a[0], a[1], a[2], ..., a[n-1]]</code> 旋转一次 的结果为数组 <code>[a[n-1], a[0], a[1], a[2], ..., a[n-2]]</code> 。



<strong>示例 1：</strong>

<pre>
<strong>输入：</strong><code>numbers = </code>[3,4,5,1,2]
<strong>输出：</strong>1
</pre>

<strong>示例 2：</strong>

<pre>
<strong>输入：</strong><code>numbers = </code>[2,2,2,0,1]
<strong>输出：</strong>0
</pre>



<strong>提示：</strong>

<ul>
	<li><code>n == numbers.length</code></li>
	<li><code>1 <= n <= 5000</code></li>
	<li><code>-5000 <= numbers[i] <= 5000</code></li>
	<li><code>numbers</code> 原来是一个升序排序的数组，并进行了 <code>1</code> 至 <code>n</code> 次旋转</li>
</ul>

注意：本题与主站 154 题相同：<a href="https://leetcode-cn.com/problems/find-minimum-in-rotated-sorted-array-ii/">https://leetcode-cn.com/problems/find-minimum-in-rotated-sorted-array-ii/</a>
