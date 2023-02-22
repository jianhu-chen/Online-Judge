# 第 98 场双周赛

> 企业: 力扣

## 2566.替换一个数字后的最大差值

[打开力扣](https://leetcode.cn/problems/maximum-difference-by-remapping-a-digit) [我的代码](2566.maximum_difference_by_remapping_a_digit.py)

给你一个整数<code>num</code>。你知道 Danny Mittal 会偷偷将 <code>0</code>到 <code>9</code>中的一个数字 <strong>替换</strong> 成另一个数字。

请你返回将 <code>num</code>中<strong>恰好一个</strong>数字进行替换后，得到的最大值和最小值的差位多少。

<strong>注意：</strong>

<ul>
	<li>当 Danny 将一个数字 <code>d1</code> 替换成另一个数字 <code>d2</code> 时，Danny 需要将<code>nums</code>中所有 <code>d1</code>都替换成<code>d2</code>。</li>
	<li>Danny 可以将一个数字替换成它自己，也就是说<code>num</code>可以不变。</li>
	<li>Danny 可以将数字分别替换成两个不同的数字分别得到最大值和最小值。</li>
	<li>替换后得到的数字可以包含前导 0 。</li>
	<li>Danny Mittal 获得周赛 326 前 10 名，让我们恭喜他。</li>
</ul>



<strong>示例 1：</strong>

<pre>
<b>输入：</b>num = 11891
<b>输出：</b>99009
<b>解释：</b>
为了得到最大值，我们将数字 1 替换成数字 9 ，得到 99899 。
为了得到最小值，我们将数字 1 替换成数字 0 ，得到 890 。
两个数字的差值为 99009 。
</pre>

<strong>示例 2：</strong>

<pre>
<b>输入：</b>num = 90
<b>输出：</b>99
<strong>解释：</strong>
可以得到的最大值是 99（将 0 替换成 9），最小值是 0（将 9 替换成 0）。
所以我们得到 99 。</pre>



<strong>提示：</strong>

<ul>
	<li><code>1 <= num <= 10<sup>8</sup></code></li>
</ul>

## 2567.修改两个元素的最小分数

[打开力扣](https://leetcode.cn/problems/minimum-score-by-changing-two-elements) [我的代码](2567.minimum_score_by_changing_two_elements.py)

给你一个下标从 <strong>0</strong>开始的整数数组<code>nums</code>。

<ul>
	<li><code>nums</code> 的 <strong>最小</strong>得分是满足 <code>0 <= i < j < nums.length</code>的<code>|nums[i]- nums[j]|</code>的最小值。</li>
	<li><code>nums</code>的 <strong>最大 </strong>得分是满足 <code>0 <= i < j < nums.length</code>的<code>|nums[i]- nums[j]|</code>的最大值。</li>
	<li><code>nums</code>的分数是 <strong>最大</strong>得分与 <strong>最小</strong>得分的和。</li>
</ul>

我们的目标是最小化<code>nums</code>的分数。你 <strong>最多</strong> 可以修改<code>nums</code>中<strong>2</strong>个元素的值。

请你返回修改<code>nums</code>中<strong>至多两个</strong>元素的值后，可以得到的 <strong>最小分数</strong>。

<code>|x|</code>表示 <code>x</code>的绝对值。



<strong>示例 1：</strong>

<pre>
<b>输入：</b>nums = [1,4,3]
<b>输出：</b>0
<b>解释：</b>将 nums[1] 和 nums[2] 的值改为 1 ，nums 变为 [1,1,1] 。<code>|nums[i] - nums[j]|</code> 的值永远为 0 ，所以我们返回 0 + 0 = 0 。
</pre>

<strong>示例 2：</strong>

<pre>
<b>输入：</b>nums = [1,4,7,8,5]
<b>输出：</b>3
<b>解释：
</b>将 nums[0] 和 nums[1] 的值变为 6 ，nums 变为 [6,6,7,8,5] 。
最小得分是 i = 0 且 j = 1 时得到的 |<code>nums[i] - nums[j]</code>| = |6 - 6| = 0 。
最大得分是 i = 3 且 j = 4 时得到的 |<code>nums[i] - nums[j]</code>| = |8 - 5| = 3 。
最大得分与最小得分之和为 3 。这是最优答案。
</pre>



<strong>提示：</strong>

<ul>
	<li><code>3 <= nums.length <= 10<sup>5</sup></code></li>
	<li><code>1 <= nums[i] <= 10<sup>9</sup></code></li>
</ul>

## 2568.最小无法得到的或值

[打开力扣](https://leetcode.cn/problems/minimum-impossible-or) [我的代码](2568.minimum_impossible_or.py)

给你一个下标从 <strong>0</strong>开始的整数数组<code>nums</code>。

如果存在一些整数满足<code>0 <= index<sub>1</sub> < index<sub>2</sub> < ... < index<sub>k</sub> < nums.length</code>，得到<code>nums[index<sub>1</sub>] | nums[index<sub>2</sub>] | ... | nums[index<sub>k</sub>] = x</code>，那么我们说<code>x</code>是<strong>可表达的</strong>。换言之，如果一个整数能由<code>nums</code>的某个子序列的或运算得到，那么它就是可表达的。

请你返回 <code>nums</code>不可表达的 <strong>最小非零整数</strong>。



<strong>示例 1：</strong>

<pre><b>输入：</b>nums = [2,1]
<b>输出：</b>4
<b>解释：</b>1 和 2 已经在数组中，因为 nums[0] | nums[1] = 2 | 1 = 3 ，所以 3 是可表达的。由于 4 是不可表达的，所以我们返回 4 。
</pre>

<strong>示例 2：</strong>

<pre><b>输入：</b>nums = [5,3,2]
<b>输出：</b>1
<b>解释：</b>1 是最小不可表达的数字。
</pre>



<strong>提示：</strong>

<ul>
	<li><code>1 <= nums.length <= 10<sup>5</sup></code></li>
	<li><code>1 <= nums[i] <= 10<sup>9</sup></code></li>
</ul>

## 2569.更新数组后处理求和查询

[打开力扣](https://leetcode.cn/problems/handling-sum-queries-after-update) [我的代码](2569.handling_sum_queries_after_update.py)

给你两个下标从 <strong>0</strong>开始的数组<code>nums1</code> 和<code>nums2</code>，和一个二维数组<code>queries</code>表示一些操作。总共有 3 种类型的操作：

<ol>
	<li>操作类型 1 为<code>queries[i]= [1, l, r]</code>。你需要将 <code>nums1</code>从下标<code>l</code>到下标 <code>r</code>的所有 <code>0</code>反转成 <code>1</code>或将 <code>1</code>反转成 <code>0</code>。<code>l</code>和 <code>r</code>下标都从 <strong>0</strong>开始。</li>
	<li>操作类型 2 为<code>queries[i]= [2, p, 0]</code>。对于<code>0 <= i < n</code>中的所有下标，令<code>nums2[i] =nums2[i]+ nums1[i]* p</code>。</li>
	<li>操作类型 3 为<code>queries[i]= [3, 0, 0]</code>。求<code>nums2</code>中所有元素的和。</li>
</ol>

请你返回一个数组，包含所有第三种操作类型的答案。



<strong>示例 1：</strong>

<pre>
<b>输入：</b>nums1 = [1,0,1], nums2 = [0,0,0], queries = [[1,1,1],[2,1,0],[3,0,0]]
<b>输出：</b>[3]
<strong>解释：</strong>第一个操作后 nums1 变为 [1,1,1] 。第二个操作后，nums2 变成 [1,1,1] ，所以第三个操作的答案为 3 。所以返回 [3] 。
</pre>

<strong>示例 2：</strong>

<pre>
<b>输入：</b>nums1 = [1], nums2 = [5], queries = [[2,0,0],[3,0,0]]
<b>输出：</b>[5]
<b>解释：</b>第一个操作后，nums2 保持不变为 [5] ，所以第二个操作的答案是 5 。所以返回 [5] 。
</pre>



<strong>提示：</strong>

<ul>
	<li><code>1 <= nums1.length,nums2.length <= 10<sup>5</sup></code></li>
	<li><code>nums1.length = nums2.length</code></li>
	<li><code>1 <= queries.length <= 10<sup>5</sup></code></li>
	<li><code>queries[i].length = 3</code></li>
	<li><code>0 <= l <= r <= nums1.length - 1</code></li>
	<li><code>0 <= p <= 10<sup>6</sup></code></li>
	<li><code>0 <= nums1[i] <= 1</code></li>
	<li><code>0 <= nums2[i] <= 10<sup>9</sup></code></li>
</ul>
