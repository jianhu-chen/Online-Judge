# 第 326 场周赛

> 企业: 力扣 LeetCode

## 2520.统计能整除数字的位数

[打开力扣](https://leetcode.cn/problems/count-the-digits-that-divide-a-number) [我的代码](2520.count_the_digits_that_divide_a_number.py)

给你一个整数 <code>num</code> ，返回 <code>num</code> 中能整除 <code>num</code> 的数位的数目。

如果满足<code>nums % val == 0</code> ，则认为整数 <code>val</code> 可以整除 <code>nums</code> 。



<strong>示例 1：</strong>

<pre><strong>输入：</strong>num = 7
<strong>输出：</strong>1
<strong>解释：</strong>7 被自己整除，因此答案是 1 。
</pre>

<strong>示例 2：</strong>

<pre><strong>输入：</strong>num = 121
<strong>输出：</strong>2
<strong>解释：</strong>121 可以被 1 整除，但无法被 2 整除。由于 1 出现两次，所以返回 2 。
</pre>

<strong>示例 3：</strong>

<pre><strong>输入：</strong>num = 1248
<strong>输出：</strong>4
<strong>解释：</strong>1248 可以被它每一位上的数字整除，因此答案是 4 。
</pre>



<strong>提示：</strong>

<ul>
	<li><code>1 <= num <= 10<sup>9</sup></code></li>
	<li><code>num</code> 的数位中不含 <code>0</code></li>
</ul>

## 2521.数组乘积中的不同质因数数目

[打开力扣](https://leetcode.cn/problems/distinct-prime-factors-of-product-of-array) [我的代码](2521.distinct_prime_factors_of_product_of_array.py)

给你一个正整数数组 <code>nums</code> ，对 <code>nums</code> 所有元素求积之后，找出并返回乘积中 <strong>不同质因数</strong> 的数目。

<strong>注意：</strong>

<ul>
	<li><strong>质数</strong> 是指大于 <code>1</code> 且仅能被 <code>1</code> 及自身整除的数字。</li>
	<li>如果 <code>val2 / val1</code> 是一个整数，则整数 <code>val1</code> 是另一个整数 <code>val2</code> 的一个因数。</li>
</ul>



<strong>示例 1：</strong>

<pre><strong>输入：</strong>nums = [2,4,3,7,10,6]
<strong>输出：</strong>4
<strong>解释：</strong>
nums 中所有元素的乘积是：2 * 4 * 3 * 7 * 10 * 6 = 10080 = 2<sup>5</sup> * 3<sup>2</sup> * 5 * 7 。
共有 4 个不同的质因数，所以返回 4 。
</pre>

<strong>示例 2：</strong>

<pre><strong>输入：</strong>nums = [2,4,8,16]
<strong>输出：</strong>1
<strong>解释：</strong>
nums 中所有元素的乘积是：2 * 4 * 8 * 16 = 1024 = 2<sup>10</sup> 。
共有 1 个不同的质因数，所以返回 1 。</pre>



<strong>提示：</strong>

<ul>
	<li><code>1 <= nums.length <= 10<sup>4</sup></code></li>
	<li><code>2 <= nums[i] <= 1000</code></li>
</ul>

## 2522.将字符串分割成值不超过 K 的子字符串

[打开力扣](https://leetcode.cn/problems/partition-string-into-substrings-with-values-at-most-k) [我的代码](2522.partition_string_into_substrings_with_values_at_most_k.py)

给你一个字符串<code>s</code>，它每一位都是<code>1</code>到<code>9</code>之间的数字组成，同时给你一个整数<code>k</code>。

如果一个字符串 <code>s</code>的分割满足以下条件，我们称它是一个 <strong>好</strong>分割：

<ul>
	<li><code>s</code>中每个数位 <strong>恰好</strong>属于一个子字符串。</li>
	<li>每个子字符串的值都小于等于<code>k</code>。</li>
</ul>

请你返回 <code>s</code>所有的 <strong>好</strong>分割中，子字符串的<strong>最少</strong>数目。如果不存在 <code>s</code>的<strong>好</strong>分割，返回<code>-1</code>。

<b>注意：</b>

<ul>
	<li>一个字符串的 <strong>值</strong>是这个字符串对应的整数。比方说，<code>"123"</code>的值为<code>123</code>，<code>"1"</code>的值是<code>1</code>。</li>
	<li><strong>子字符串</strong>是字符串中一段连续的字符序列。</li>
</ul>



<strong>示例 1：</strong>

<pre>
<b>输入：</b>s = "165462", k = 60
<b>输出：</b>4
<b>解释：</b>我们将字符串分割成子字符串 "16" ，"54" ，"6" 和 "2" 。每个子字符串的值都小于等于 k = 60 。
不存在小于 4 个子字符串的好分割。
</pre>

<strong>示例 2：</strong>

<pre>
<b>输入：</b>s = "238182", k = 5
<b>输出：</b>-1
<strong>解释：</strong>这个字符串不存在好分割。
</pre>



<strong>提示：</strong>

<ul>
	<li><code>1 <= s.length <= 10<sup>5</sup></code></li>
	<li><code>s[i]</code>是<code>'1'</code>到<code>'9'</code>之间的数字。</li>
	<li><code>1 <= k <= 10<sup>9</sup></code></li>
</ul>

## 2523.范围内最接近的两个质数

[打开力扣](https://leetcode.cn/problems/closest-prime-numbers-in-range) [我的代码](2523.closest_prime_numbers_in_range.py)

给你两个正整数<code>left</code> 和<code>right</code>，请你找到两个整数<code>num1</code> 和<code>num2</code>，它们满足：

<ul>
	<li><code>left <= nums1 < nums2 <= right</code>。</li>
	<li><code>nums1</code> 和<code>nums2</code>都是 <strong>质数</strong>。</li>
	<li><code>nums2 - nums1</code>是满足上述条件的质数对中的 <strong>最小值</strong>。</li>
</ul>

请你返回正整数数组<code>ans = [nums1, nums2]</code>。如果有多个整数对满足上述条件，请你返回<code>nums1</code>最小的质数对。如果不存在符合题意的质数对，请你返回<code>[-1, -1]</code>。

如果一个整数大于<code>1</code>，且只能被<code>1</code> 和它自己整除，那么它是一个质数。



<strong>示例 1：</strong>

<pre>
<b>输入：</b>left = 10, right = 19
<b>输出：</b>[11,13]
<b>解释：</b>10 到 19 之间的质数为 11 ，13 ，17 和 19 。
质数对的最小差值是 2 ，[11,13] 和 [17,19] 都可以得到最小差值。
由于 11 比 17 小，我们返回第一个质数对。
</pre>

<strong>示例 2：</strong>

<pre>
<b>输入：</b>left = 4, right = 6
<b>输出：</b>[-1,-1]
<b>解释：</b>给定范围内只有一个质数，所以题目条件无法被满足。
</pre>



<strong>提示：</strong>

<ul>
	<li><code>1 <= left <= right <= 10<sup>6</sup></code></li>
</ul>
