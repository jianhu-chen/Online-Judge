# 第 337 场周赛

> 企业: 力扣 LeetCode

## 2595.奇偶位数

[打开力扣](https://leetcode.cn/problems/number-of-even-and-odd-bits) [我的代码](2595.number_of_even_and_odd_bits.py)

给你一个 <strong>正</strong> 整数 <code>n</code> 。

用 <code>even</code> 表示在 <code>n</code> 的二进制形式（下标从 <strong>0</strong> 开始）中值为 <code>1</code> 的偶数下标的个数。

用 <code>odd</code> 表示在 <code>n</code> 的二进制形式（下标从 <strong>0</strong> 开始）中值为 <code>1</code> 的奇数下标的个数。

返回整数数组<em> </em><code>answer</code><em> </em>，其中<em> </em><code>answer = [even, odd]</code> 。



<strong>示例 1：</strong>

<pre><strong>输入：</strong>n = 17
<strong>输出：</strong>[2,0]
<strong>解释：</strong>17 的二进制形式是 10001 。
下标 0 和 下标 4 对应的值为 1 。
共有 2 个偶数下标，0 个奇数下标。
</pre>

<strong>示例 2：</strong>

<pre><strong>输入：</strong>n = 2
<strong>输出：</strong>[0,1]
<strong>解释：</strong>2 的二进制形式是 10 。
下标 1 对应的值为 1 。
共有 0 个偶数下标，1 个奇数下标。
</pre>



<strong>提示：</strong>

<ul>
	<li><code>1 <= n <= 1000</code></li>
</ul>

## 2596.检查骑士巡视方案

[打开力扣](https://leetcode.cn/problems/check-knight-tour-configuration) [我的代码](2596.check_knight_tour_configuration.py)

骑士在一张 <code>n x n</code> 的棋盘上巡视。在有效的巡视方案中，骑士会从棋盘的 <strong>左上角</strong> 出发，并且访问棋盘上的每个格子 <strong>恰好一次</strong> 。

给你一个 <code>n x n</code> 的整数矩阵 <code>grid</code> ，由范围 <code>[0, n * n - 1]</code> 内的不同整数组成，其中 <code>grid[row][col]</code> 表示单元格 <code>(row, col)</code> 是骑士访问的第 <code>grid[row][col]</code> 个单元格。骑士的行动是从下标 <strong>0</strong> 开始的。

如果 <code>grid</code> 表示了骑士的有效巡视方案，返回 <code>true</code>；否则返回 <code>false</code>。

<strong>注意</strong>，骑士行动时可以垂直移动两个格子且水平移动一个格子，或水平移动两个格子且垂直移动一个格子。下图展示了骑士从某个格子出发可能的八种行动路线。<br>
<img alt="" src="https://assets.leetcode.com/uploads/2018/10/12/knight.png" style="width: 300px; height: 300px;">



<strong>示例 1：</strong>
<img alt="" src="https://assets.leetcode.com/uploads/2022/12/28/yetgriddrawio-5.png" style="width: 251px; height: 251px;">
<pre><strong>输入：</strong>grid = [[0,11,16,5,20],[17,4,19,10,15],[12,1,8,21,6],[3,18,23,14,9],[24,13,2,7,22]]
<strong>输出：</strong>true
<strong>解释：</strong>grid 如上图所示，可以证明这是一个有效的巡视方案。
</pre>

<strong>示例 2：</strong>
<img alt="" src="https://assets.leetcode.com/uploads/2022/12/28/yetgriddrawio-6.png" style="width: 151px; height: 151px;">
<pre><strong>输入：</strong>grid = [[0,3,6],[5,8,1],[2,7,4]]
<strong>输出：</strong>false
<strong>解释：</strong>grid 如上图所示，考虑到骑士第 7 次行动后的位置，第 8 次行动是无效的。
</pre>



<strong>提示：</strong>

<ul>
	<li><code>n == grid.length == grid[i].length</code></li>
	<li><code>3 <= n <= 7</code></li>
	<li><code>0 <= grid[row][col] < n * n</code></li>
	<li><code>grid</code> 中的所有整数 <strong>互不相同</strong></li>
</ul>

## 2597.美丽子集的数目

[打开力扣](https://leetcode.cn/problems/the-number-of-beautiful-subsets) [我的代码](2597.the_number_of_beautiful_subsets.py)

给你一个由正整数组成的数组 <code>nums</code> 和一个 <strong>正</strong> 整数 <code>k</code> 。

如果 <code>nums</code> 的子集中，任意两个整数的绝对差均不等于 <code>k</code> ，则认为该子数组是一个 <strong>美丽</strong> 子集。

返回数组 <code>nums</code> 中 <strong>非空</strong> 且 <strong>美丽</strong> 的子集数目。

<code>nums</code> 的子集定义为：可以经由 <code>nums</code> 删除某些元素（也可能不删除）得到的一个数组。只有在删除元素时选择的索引不同的情况下，两个子集才会被视作是不同的子集。



<strong>示例 1：</strong>

<pre><strong>输入：</strong>nums = [2,4,6], k = 2
<strong>输出：</strong>4
<strong>解释：</strong>数组 nums 中的美丽子集有：[2], [4], [6], [2, 6] 。
可以证明数组 [2,4,6] 中只存在 4 个美丽子集。
</pre>

<strong>示例 2：</strong>

<pre><strong>输入：</strong>nums = [1], k = 1
<strong>输出：</strong>1
<strong>解释：</strong>数组 nums 中的美丽数组有：[1] 。
可以证明数组 [1] 中只存在 1 个美丽子集。
</pre>



<strong>提示：</strong>

<ul>
	<li><code>1 <= nums.length <= 20</code></li>
	<li><code>1 <= nums[i], k <= 1000</code></li>
</ul>

## 2598.执行操作后的最大 MEX

[打开力扣](https://leetcode.cn/problems/smallest-missing-non-negative-integer-after-operations) [我的代码](2598.smallest_missing_non_negative_integer_after_operations.py)

给你一个下标从 <strong>0</strong> 开始的整数数组 <code>nums</code> 和一个整数 <code>value</code> 。

在一步操作中，你可以对 <code>nums</code> 中的任一元素加上或减去 <code>value</code> 。

<ul>
	<li>例如，如果 <code>nums = [1,2,3]</code> 且 <code>value = 2</code> ，你可以选择 <code>nums[0]</code> 减去 <code>value</code> ，得到 <code>nums = [-1,2,3]</code> 。</li>
</ul>

数组的 MEX (minimum excluded) 是指其中数组中缺失的最小非负整数。

<ul>
	<li>例如，<code>[-1,2,3]</code> 的 MEX 是 <code>0</code> ，而 <code>[1,0,3]</code> 的 MEX 是 <code>2</code> 。</li>
</ul>

返回在执行上述操作 <strong>任意次</strong> 后，<code>nums</code><em> </em>的最大 MEX <em>。</em>



<strong>示例 1：</strong>

<pre><strong>输入：</strong>nums = [1,-10,7,13,6,8], value = 5
<strong>输出：</strong>4
<strong>解释：</strong>执行下述操作可以得到这一结果：
- nums[1] 加上 value 两次，nums = [1,<em><strong>0</strong></em>,7,13,6,8]
- nums[2] 减去 value 一次，nums = [1,0,<em><strong>2</strong></em>,13,6,8]
- nums[3] 减去 value 两次，nums = [1,0,2,<em><strong>3</strong></em>,6,8]
nums 的 MEX 是 4 。可以证明 4 是可以取到的最大 MEX 。
</pre>

<strong>示例 2：</strong>

<pre><strong>输入：</strong>nums = [1,-10,7,13,6,8], value = 7
<strong>输出：</strong>2
<strong>解释：</strong>执行下述操作可以得到这一结果：
- nums[2] 减去 value 一次，nums = [1,-10,<em><strong>0</strong></em>,13,6,8]
nums 的 MEX 是 2 。可以证明 2 是可以取到的最大 MEX 。
</pre>



<strong>提示：</strong>

<ul>
	<li><code>1 <= nums.length, value <= 10<sup>5</sup></code></li>
	<li><code>-10<sup>9</sup> <= nums[i] <= 10<sup>9</sup></code></li>
</ul>
