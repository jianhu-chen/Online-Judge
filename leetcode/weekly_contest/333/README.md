# 第 333 场周赛

> 企业: 佳期投资

## 2570.合并两个二维数组 - 求和法

[打开力扣](https://leetcode.cn/problems/merge-two-2d-arrays-by-summing-values) [我的代码](2570.merge_two_2d_arrays_by_summing_values.py)

给你两个 <strong>二维</strong> 整数数组 <code>nums1</code> 和 <code>nums2.</code>

<ul>
	<li><code>nums1[i] = [id<sub>i</sub>, val<sub>i</sub>]</code> 表示编号为 <code>id<sub>i</sub></code> 的数字对应的值等于 <code>val<sub>i</sub></code> 。</li>
	<li><code>nums2[i] = [id<sub>i</sub>, val<sub>i</sub>]</code>表示编号为 <code>id<sub>i</sub></code> 的数字对应的值等于 <code>val<sub>i</sub></code> 。</li>
</ul>

每个数组都包含 <strong>互不相同</strong> 的 id ，并按 id 以 <strong>递增</strong> 顺序排列。

请你将两个数组合并为一个按 id 以递增顺序排列的数组，并符合下述条件：

<ul>
	<li>只有在两个数组中至少出现过一次的 id 才能包含在结果数组内。</li>
	<li>每个 id 在结果数组中 <strong>只能出现一次</strong> ，并且其对应的值等于两个数组中该 id 所对应的值求和。如果某个数组中不存在该 id ，则认为其对应的值等于 <code>0</code> 。</li>
</ul>

返回结果数组。返回的数组需要按 id 以递增顺序排列。



<strong>示例 1：</strong>

<pre><strong>输入：</strong>nums1 = [[1,2],[2,3],[4,5]], nums2 = [[1,4],[3,2],[4,1]]
<strong>输出：</strong>[[1,6],[2,3],[3,2],[4,6]]
<strong>解释：</strong>结果数组中包含以下元素：
- id = 1 ，对应的值等于 2 + 4 = 6 。
- id = 2 ，对应的值等于 3 。
- id = 3 ，对应的值等于 2 。
- id = 4 ，对应的值等于5 + 1 = 6 。
</pre>

<strong>示例 2：</strong>

<pre><strong>输入：</strong>nums1 = [[2,4],[3,6],[5,5]], nums2 = [[1,3],[4,3]]
<strong>输出：</strong>[[1,3],[2,4],[3,6],[4,3],[5,5]]
<strong>解释：</strong>不存在共同 id ，在结果数组中只需要包含每个 id 和其对应的值。
</pre>



<strong>提示：</strong>

<ul>
	<li><code>1 <= nums1.length, nums2.length <= 200</code></li>
	<li><code>nums1[i].length == nums2[j].length == 2</code></li>
	<li><code>1 <= id<sub>i</sub>, val<sub>i</sub> <= 1000</code></li>
	<li>数组中的 id 互不相同</li>
	<li>数据均按 id 以严格递增顺序排列</li>
</ul>

## 2571.将整数减少到零需要的最少操作数

[打开力扣](https://leetcode.cn/problems/minimum-operations-to-reduce-an-integer-to-0) [我的代码](2571.minimum_operations_to_reduce_an_integer_to_0.py)

给你一个正整数 <code>n</code> ，你可以执行下述操作 <strong>任意</strong> 次：

<ul>
	<li><code>n</code> 加上或减去 <code>2</code> 的某个 <strong>幂</strong></li>
</ul>

返回使 <code>n</code> 等于 <code>0</code> 需要执行的 <strong>最少</strong> 操作数。

如果 <code>x == 2<sup>i</sup></code> 且其中 <code>i >= 0</code> ，则数字 <code>x</code> 是 <code>2</code> 的幂。



<strong>示例 1：</strong>

<pre>
<strong>输入：</strong>n = 39
<strong>输出：</strong>3
<strong>解释：</strong>我们可以执行下述操作：
- n 加上 2<sup>0</sup> = 1 ，得到 n = 40 。
- n 减去 2<sup>3</sup> = 8 ，得到 n = 32 。
- n 减去 2<sup>5</sup> = 32 ，得到 n = 0 。
可以证明使 n 等于 0 需要执行的最少操作数是 3 。
</pre>

<strong>示例 2：</strong>

<pre>
<strong>输入：</strong>n = 54
<strong>输出：</strong>3
<strong>解释：</strong>我们可以执行下述操作：
- n 加上 2<sup>1</sup> = 2 ，得到 n = 56 。
- n 加上 2<sup>3</sup> = 8 ，得到 n = 64 。
- n 减去 2<sup>6</sup> = 64 ，得到 n = 0 。
使 n 等于 0 需要执行的最少操作数是 3 。
</pre>



<strong>提示：</strong>

<ul>
	<li><code>1 <= n <= 10<sup>5</sup></code></li>
</ul>

## 2572.无平方子集计数

[打开力扣](https://leetcode.cn/problems/count-the-number-of-square-free-subsets) [我的代码](2572.count_the_number_of_square_free_subsets.py)

给你一个正整数数组 <code>nums</code> 。

如果数组 <code>nums</code> 的子集中的元素乘积是一个 <strong>无平方因子数</strong> ，则认为该子集是一个 <strong>无平方</strong> 子集。

<strong>无平方因子数</strong> 是无法被除 <code>1</code> 之外任何平方数整除的数字。

返回数组 <code>nums</code> 中 <strong>无平方</strong> 且 <strong>非空</strong> 的子集数目。因为答案可能很大，返回对 <code>10<sup>9</sup> + 7</code> 取余的结果。

<code>nums</code> 的 <strong>非空子集</strong> 是可以由删除 <code>nums</code> 中一些元素（可以不删除，但不能全部删除）得到的一个数组。如果构成两个子集时选择删除的下标不同，则认为这两个子集不同。



<strong>示例 1：</strong>

<pre>
<strong>输入：</strong>nums = [3,4,4,5]
<strong>输出：</strong>3
<strong>解释：</strong>示例中有 3 个无平方子集：
- 由第 0 个元素 [3] 组成的子集。其元素的乘积是 3 ，这是一个无平方因子数。
- 由第 3 个元素 [5] 组成的子集。其元素的乘积是 5 ，这是一个无平方因子数。
- 由第 0 个和第 3 个元素 [3,5] 组成的子集。其元素的乘积是 15 ，这是一个无平方因子数。
可以证明给定数组中不存在超过 3 个无平方子集。</pre>

<strong>示例 2：</strong>

<pre>
<strong>输入：</strong>nums = [1]
<strong>输出：</strong>1
<strong>解释：</strong>示例中有 1 个无平方子集：
- 由第 0 个元素 [1] 组成的子集。其元素的乘积是 1 ，这是一个无平方因子数。
可以证明给定数组中不存在超过 1 个无平方子集。</pre>



<strong>提示：</strong>

<ul>
	<li><code>1 <= nums.length<= 1000</code></li>
	<li><code>1 <= nums[i] <= 30</code></li>
</ul>

## 2573.找出对应 LCP 矩阵的字符串

[打开力扣](https://leetcode.cn/problems/find-the-string-with-lcp) [我的代码](2573.find_the_string_with_lcp.py)

对任一由 <code>n</code> 个小写英文字母组成的字符串 <code>word</code> ，我们可以定义一个 <code>n x n</code> 的矩阵，并满足：

<ul>
	<li><code>lcp[i][j]</code> 等于子字符串<code>word[i,...,n-1]</code> 和 <code>word[j,...,n-1]</code> 之间的最长公共前缀的长度。</li>
</ul>

给你一个 <code>n x n</code> 的矩阵 <code>lcp</code> 。返回与 <code>lcp</code> 对应的、按字典序最小的字符串<code>word</code> 。如果不存在这样的字符串，则返回空字符串。

对于长度相同的两个字符串 <code>a</code> 和 <code>b</code> ，如果在 <code>a</code> 和 <code>b</code> 不同的第一个位置，字符串 <code>a</code> 的字母在字母表中出现的顺序先于 <code>b</code> 中的对应字母，则认为字符串 <code>a</code> 按字典序比字符串 <code>b</code> 小。例如，<code>"aabd"</code> 在字典上小于 <code>"aaca"</code> ，因为二者不同的第一位置是第三个字母，而<code>'b'</code> 先于 <code>'c'</code> 出现。



<strong>示例 1：</strong>

<pre>
<strong>输入：</strong>lcp = [[4,0,2,0],[0,3,0,1],[2,0,2,0],[0,1,0,1]]
<strong>输出：</strong>"abab"
<strong>解释：</strong>lcp 对应由两个交替字母组成的任意 4 字母字符串，字典序最小的是 "abab" 。
</pre>

<strong>示例 2：</strong>

<pre>
<strong>输入：</strong>lcp = [[4,3,2,1],[3,3,2,1],[2,2,2,1],[1,1,1,1]]
<strong>输出：</strong>"aaaa"
<strong>解释：</strong>lcp 对应只有一个不同字母的任意 4 字母字符串，字典序最小的是 "aaaa" 。
</pre>

<strong>示例 3：</strong>

<pre>
<strong>输入：</strong>lcp = [[4,3,2,1],[3,3,2,1],[2,2,2,1],[1,1,1,3]]
<strong>输出：</strong>""
<strong>解释：</strong>lcp[3][3] 无法等于 3 ，因为 word[3,...,3] 仅由单个字母组成；因此，不存在答案。
</pre>



<strong>提示：</strong>

<ul>
	<li><code>1 <= n ==</code><code>lcp.length == </code><code>lcp[i].length</code><code><= 1000</code></li>
	<li><code><font face="monospace">0 <= lcp[i][j] <= n</font></code></li>
</ul>
