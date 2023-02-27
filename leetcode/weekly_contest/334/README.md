# 第 334 场周赛

> 企业: 力扣 LeetCode

## 6369.左右元素和的差值

[打开力扣](https://leetcode.cn/problems/left-and-right-sum-differences) [我的代码](6369.left_and_right_sum_differences.py)

给你一个下标从 <strong>0</strong> 开始的整数数组 <code>nums</code> ，请你找出一个下标从 <strong>0</strong> 开始的整数数组 <code>answer</code> ，其中：

<ul>
	<li><code>answer.length == nums.length</code></li>
	<li><code>answer[i] = |leftSum[i] - rightSum[i]|</code></li>
</ul>

其中：

<ul>
	<li><code>leftSum[i]</code> 是数组 <code>nums</code> 中下标 <code>i</code> 左侧元素之和。如果不存在对应的元素，<code>leftSum[i] = 0</code> 。</li>
	<li><code>rightSum[i]</code> 是数组 <code>nums</code> 中下标 <code>i</code> 右侧元素之和。如果不存在对应的元素，<code>rightSum[i] = 0</code> 。</li>
</ul>

返回数组 <code>answer</code> 。



<strong>示例 1：</strong>

<pre><strong>输入：</strong>nums = [10,4,8,3]
<strong>输出：</strong>[15,1,11,22]
<strong>解释：</strong>数组 leftSum 为 [0,10,14,22] 且数组 rightSum 为 [15,11,3,0] 。
数组 answer 为 [|0 - 15|,|10 - 11|,|14 - 3|,|22 - 0|] = [15,1,11,22] 。
</pre>

<strong>示例 2：</strong>

<pre><strong>输入：</strong>nums = [1]
<strong>输出：</strong>[0]
<strong>解释：</strong>数组 leftSum 为 [0] 且数组 rightSum 为 [0] 。
数组 answer 为 [|0 - 0|] = [0] 。
</pre>



<strong>提示：</strong>

<ul>
	<li><code>1 <= nums.length <= 1000</code></li>
	<li><code>1 <= nums[i] <= 10<sup>5</sup></code></li>
</ul>

## 6368.找出字符串的可整除数组

[打开力扣](https://leetcode.cn/problems/find-the-divisibility-array-of-a-string) [我的代码](6368.find_the_divisibility_array_of_a_string.py)

给你一个下标从 <strong>0</strong> 开始的字符串 <code>word</code> ，长度为 <code>n</code> ，由从 <code>0</code> 到 <code>9</code> 的数字组成。另给你一个正整数 <code>m</code> 。

<code>word</code> 的 <strong>可整除数组</strong> <code>div</code> 是一个长度为 <code>n</code> 的整数数组，并满足：

<ul>
	<li>如果 <code>word[0,...,i]</code> 所表示的 <strong>数值</strong> 能被 <code>m</code> 整除，<code>div[i] = 1</code></li>
	<li>否则，<code>div[i] = 0</code></li>
</ul>

返回<em> </em><code>word</code> 的可整除数组。



<strong>示例 1：</strong>

<pre>
<strong>输入：</strong>word = "998244353", m = 3
<strong>输出：</strong>[1,1,0,0,0,1,1,0,0]
<strong>解释：</strong>仅有 4 个前缀可以被 3 整除："9"、"99"、"998244" 和 "9982443" 。
</pre>

<strong>示例 2：</strong>

<pre>
<strong>输入：</strong>word = "1010", m = 10
<strong>输出：</strong>[0,1,0,1]
<strong>解释：</strong>仅有 2 个前缀可以被 10 整除："10" 和 "1010" 。
</pre>



<strong>提示：</strong>

<ul>
	<li><code>1 <= n <= 10<sup>5</sup></code></li>
	<li><code>word.length == n</code></li>
	<li><code>word</code> 由数字 <code>0</code> 到 <code>9</code> 组成</li>
	<li><code>1 <= m <= 10<sup>9</sup></code></li>
</ul>

## 6367.求出最多标记下标

[打开力扣](https://leetcode.cn/problems/find-the-maximum-number-of-marked-indices) [我的代码](6367.find_the_maximum_number_of_marked_indices.py)

给你一个下标从 <strong>0</strong>开始的整数数组<code>nums</code>。

一开始，所有下标都没有被标记。你可以执行以下操作任意次：

<ul>
	<li>选择两个 <strong>互不相同且未标记</strong>的下标<code>i</code> 和<code>j</code>，满足<code>2 * nums[i] <= nums[j]</code>，标记下标<code>i</code> 和<code>j</code>。</li>
</ul>

请你执行上述操作任意次，返回<em></em><code>nums</code>中最多可以标记的下标数目。



<strong>示例 1：</strong>

<pre>
<b>输入：</b>nums = [3,5,2,4]
<b>输出：</b>2
<strong>解释：</strong>第一次操作中，选择 i = 2 和 j = 1 ，操作可以执行的原因是 2 * nums[2] <= nums[1] ，标记下标 2 和 1 。
没有其他更多可执行的操作，所以答案为 2 。
</pre>

<strong>示例 2：</strong>

<pre>
<b>输入：</b>nums = [9,2,5,4]
<b>输出：</b>4
<strong>解释：</strong>第一次操作中，选择 i = 3 和 j = 0 ，操作可以执行的原因是 2 * nums[3] <= nums[0] ，标记下标 3 和 0 。
第二次操作中，选择 i = 1 和 j = 2 ，操作可以执行的原因是 2 * nums[1] <= nums[2] ，标记下标 1 和 2 。
没有其他更多可执行的操作，所以答案为 4 。
</pre>

<strong>示例 3：</strong>

<pre>
<b>输入：</b>nums = [7,6,8]
<b>输出：</b>0
<strong>解释：</strong>没有任何可以执行的操作，所以答案为 0 。
</pre>



<strong>提示：</strong>

<ul>
	<li><code>1 <= nums.length <= 10<sup>5</sup></code></li>
	<li><code>1 <= nums[i] <= 10<sup>9</sup></code></li>
</ul>

## 6366.在网格图中访问一个格子的最少时间

[打开力扣](https://leetcode.cn/problems/minimum-time-to-visit-a-cell-in-a-grid) [我的代码](6366.minimum_time_to_visit_a_cell_in_a_grid.py)

给你一个<code>m x n</code>的矩阵<code>grid</code>，每个元素都为 <strong>非负</strong>整数，其中<code>grid[row][col]</code>表示可以访问格子<code>(row, col)</code>的<strong>最早</strong>时间。也就是说当你访问格子<code>(row, col)</code>时，最少已经经过的时间为<code>grid[row][col]</code>。

你从 <strong>最左上角</strong>出发，出发时刻为 <code>0</code>，你必须一直移动到上下左右相邻四个格子中的 <strong>任意</strong>一个格子（即不能停留在格子上）。每次移动都需要花费 1 单位时间。

请你返回 <strong>最早</strong>到达右下角格子的时间，如果你无法到达右下角的格子，请你返回 <code>-1</code>。



<strong>示例 1：</strong>

<img alt="" src="https://assets.leetcode.com/uploads/2023/02/14/yetgriddrawio-8.png" />

<pre>
<b>输入：</b>grid = [[0,1,3,2],[5,1,2,5],[4,3,8,6]]
<b>输出：</b>7
<b>解释：</b>一条可行的路径为：
- 时刻 t = 0 ，我们在格子 (0,0) 。
- 时刻 t = 1 ，我们移动到格子 (0,1) ，可以移动的原因是 grid[0][1] <= 1 。
- 时刻 t = 2 ，我们移动到格子 (1,1) ，可以移动的原因是 grid[1][1] <= 2 。
- 时刻 t = 3 ，我们移动到格子 (1,2) ，可以移动的原因是 grid[1][2] <= 3 。
- 时刻 t = 4 ，我们移动到格子 (1,1) ，可以移动的原因是 grid[1][1] <= 4 。
- 时刻 t = 5 ，我们移动到格子 (1,2) ，可以移动的原因是 grid[1][2] <= 5 。
- 时刻 t = 6 ，我们移动到格子 (1,3) ，可以移动的原因是 grid[1][3] <= 6 。
- 时刻 t = 7 ，我们移动到格子 (2,3) ，可以移动的原因是 grid[2][3] <= 7 。
最终到达时刻为 7 。这是最早可以到达的时间。
</pre>

<strong>示例 2：</strong>

<img alt="" src="https://assets.leetcode.com/uploads/2023/02/14/yetgriddrawio-9.png" style="width: 151px; height: 151px;" />

<pre>
<b>输入：</b>grid = [[0,2,4],[3,2,1],[1,0,4]]
<b>输出：</b>-1
<b>解释：</b>没法从左上角按题目规定走到右下角。
</pre>



<strong>提示：</strong>

<ul>
	<li><code>m == grid.length</code></li>
	<li><code>n == grid[i].length</code></li>
	<li><code>2 <= m, n <= 1000</code></li>
	<li><code>4 <= m * n <= 10<sup>5</sup></code></li>
	<li><code>0 <= grid[i][j] <= 10<sup>5</sup></code></li>
	<li><code>grid[0][0] == 0</code></li>
</ul>
