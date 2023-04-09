# 第 340 场周赛

> 企业: 力扣

## 6361.对角线上的质数

[打开力扣](https://leetcode.cn/problems/prime-in-diagonal) [我的代码](6361.prime_in_diagonal.py)

给你一个下标从 <strong>0</strong> 开始的二维整数数组 <code>nums</code> 。

返回位于 <code>nums</code> 至少一条 <strong>对角线</strong> 上的最大 <strong>质数</strong> 。如果任一对角线上均不存在质数，返回<em> 0 。</em>

注意：

<ul>
	<li>如果某个整数大于 <code>1</code> ，且不存在除 <code>1</code> 和自身之外的正整数因子，则认为该整数是一个质数。</li>
	<li>如果存在整数 <code>i</code> ，使得<code>nums[i][i] = val</code> 或者<code>nums[i][nums.length - i - 1]= val</code> ，则认为整数 <code>val</code> 位于 <code>nums</code> 的一条对角线上。</li>
</ul>

<img alt="" src="https://assets.leetcode.com/uploads/2023/03/06/screenshot-2023-03-06-at-45648-pm.png" style="width: 181px; height: 121px;" />

在上图中，一条对角线是 <strong>[1,5,9]</strong> ，而另一条对角线是<strong> [3,5,7]</strong> 。



<strong>示例 1：</strong>

<pre>
<strong>输入：</strong>nums = [[1,2,3],[5,6,7],[9,10,11]]
<strong>输出：</strong>11
<strong>解释：</strong>数字 1、3、6、9 和 11 是所有 "位于至少一条对角线上" 的数字。由于 11 是最大的质数，故返回 11 。
</pre>

<strong>示例 2：</strong>

<pre>
<strong>输入：</strong>nums = [[1,2,3],[5,17,7],[9,11,10]]
<strong>输出：</strong>17
<strong>解释：</strong>数字 1、3、9、10 和 17 是所有满足"位于至少一条对角线上"的数字。由于 17 是最大的质数，故返回 17 。
</pre>



<strong>提示：</strong>

<ul>
	<li><code>1 <= nums.length <= 300</code></li>
	<li><code>nums.length == nums<sub>i</sub>.length</code></li>
	<li><code>1 <= nums<span style="">[i][j]</span><= 4*10<sup>6</sup></code></li>
</ul>

## 6360.等值距离和

[打开力扣](https://leetcode.cn/problems/sum-of-distances) [我的代码](6360.sum_of_distances.py)

给你一个下标从 <strong>0</strong> 开始的整数数组 <code>nums</code> 。现有一个长度等于 <code>nums.length</code> 的数组 <code>arr</code> 。对于满足 <code>nums[j] == nums[i]</code> 且 <code>j != i</code> 的所有 <code>j</code> ，<code>arr[i]</code> 等于所有 <code>|i - j|</code> 之和。如果不存在这样的 <code>j</code> ，则令 <code>arr[i]</code> 等于 <code>0</code> 。

返回数组<em> </em><code>arr</code><em> 。</em>



<strong>示例 1：</strong>

<pre>
<strong>输入：</strong>nums = [1,3,1,1,2]
<strong>输出：</strong>[5,0,3,4,0]
<strong>解释：</strong>
i = 0 ，nums[0] == nums[2] 且 nums[0] == nums[3] 。因此，arr[0] = |0 - 2| + |0 - 3| = 5 。 
i = 1 ，arr[1] = 0 因为不存在值等于 3 的其他下标。
i = 2 ，nums[2] == nums[0] 且 nums[2] == nums[3] 。因此，arr[2] = |2 - 0| + |2 - 3| = 3 。
i = 3 ，nums[3] == nums[0] 且 nums[3] == nums[2] 。因此，arr[3] = |3 - 0| + |3 - 2| = 4 。 
i = 4 ，arr[4] = 0 因为不存在值等于 2 的其他下标。
</pre>

<strong>示例 2：</strong>

<pre>
<strong>输入：</strong>nums = [0,5,3]
<strong>输出：</strong>[0,0,0]
<strong>解释：</strong>因为 nums 中的元素互不相同，对于所有 i ，都有 arr[i] = 0 。
</pre>



<strong>提示：</strong>

<ul>
	<li><code>1 <= nums.length <= 10<sup>5</sup></code></li>
	<li><code>0 <= nums[i] <= 10<sup>9</sup></code></li>
</ul>

## 6359.最小化数对的最大差值

[打开力扣](https://leetcode.cn/problems/minimize-the-maximum-difference-of-pairs) [我的代码](6359.minimize_the_maximum_difference_of_pairs.py)

给你一个下标从 <strong>0</strong>开始的整数数组<code>nums</code>和一个整数<code>p</code>。请你从<code>nums</code>中找到<code>p</code> 个下标对，每个下标对对应数值取差值，你需要使得这 <code>p</code> 个差值的<strong>最大值</strong><strong>最小</strong>。同时，你需要确保每个下标在这<code>p</code>个下标对中最多出现一次。

对于一个下标对<code>i</code>和<code>j</code>，这一对的差值为<code>|nums[i] - nums[j]|</code>，其中<code>|x|</code>表示 <code>x</code>的 <strong>绝对值</strong>。

请你返回 <code>p</code>个下标对对应数值 <strong>最大差值</strong>的 <strong>最小值</strong>。



<strong>示例 1：</strong>

<pre>
<b>输入：</b>nums = [10,1,2,7,1,3], p = 2
<b>输出：</b>1
<b>解释：</b>第一个下标对选择 1 和 4 ，第二个下标对选择 2 和 5 。
最大差值为 max(|nums[1] - nums[4]|, |nums[2] - nums[5]|) = max(0, 1) = 1 。所以我们返回 1 。
</pre>

<strong>示例 2：</strong>

<pre>
<b>输入：</b>nums = [4,2,1,2], p = 1
<b>输出：</b>0
<b>解释：</b>选择下标 1 和 3 构成下标对。差值为 |2 - 2| = 0 ，这是最大差值的最小值。
</pre>



<strong>提示：</strong>

<ul>
	<li><code>1 <= nums.length <= 10<sup>5</sup></code></li>
	<li><code>0 <= nums[i] <= 10<sup>9</sup></code></li>
	<li><code>0 <= p <= (nums.length)/2</code></li>
</ul>

## 6353.网格图中最少访问的格子数

[打开力扣](https://leetcode.cn/problems/minimum-number-of-visited-cells-in-a-grid) [我的代码](6353.minimum_number_of_visited_cells_in_a_grid.py)

给你一个下标从 <strong>0</strong>开始的<code>m x n</code>整数矩阵<code>grid</code>。你一开始的位置在<strong>左上角</strong>格子<code>(0, 0)</code>。

当你在格子<code>(i, j)</code>的时候，你可以移动到以下格子之一：

<ul>
	<li>满足 <code>j < k <= grid[i][j] + j</code>的格子<code>(i, k)</code>（向右移动），或者</li>
	<li>满足 <code>i < k <= grid[i][j] + i</code>的格子<code>(k, j)</code>（向下移动）。</li>
</ul>

请你返回到达 <strong>右下角</strong>格子<code>(m - 1, n - 1)</code>需要经过的最少移动格子数，如果无法到达右下角格子，请你返回<code>-1</code>。



<strong>示例 1：</strong>

<img alt="" src="https://assets.leetcode.com/uploads/2023/01/25/ex1.png" style="width: 271px; height: 171px;">

<pre><b>输入：</b>grid = [[3,4,2,1],[4,2,3,1],[2,1,0,0],[2,4,0,0]]
<b>输出：</b>4
<b>解释：</b>上图展示了到达右下角格子经过的 4 个格子。
</pre>

<strong>示例 2：</strong>

<img alt="" src="https://assets.leetcode.com/uploads/2023/01/25/ex2.png" style="width: 271px; height: 171px;">

<pre><b>输入：</b>grid = [[3,4,2,1],[4,2,1,1],[2,1,1,0],[3,4,1,0]]
<b>输出：</b>3
<strong>解释：</strong>上图展示了到达右下角格子经过的 3 个格子。
</pre>

<strong>示例 3：</strong>

<img alt="" src="https://assets.leetcode.com/uploads/2023/01/26/ex3.png" style="width: 181px; height: 81px;">

<pre><b>输入：</b>grid = [[2,1,0],[1,0,0]]
<b>输出：</b>-1
<b>解释：</b>无法到达右下角格子。
</pre>



<strong>提示：</strong>

<ul>
	<li><code>m == grid.length</code></li>
	<li><code>n == grid[i].length</code></li>
	<li><code>1 <= m, n <= 10<sup>5</sup></code></li>
	<li><code>1 <= m * n <= 10<sup>5</sup></code></li>
	<li><code>0 <= grid[i][j] < m * n</code></li>
	<li><code>grid[m - 1][n - 1] == 0</code></li>
</ul>
