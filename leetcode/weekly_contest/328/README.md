# 第 328 场周赛

> 企业: 力扣

## 2535.数组元素和与数字和的绝对差

[打开力扣](https://leetcode.cn/problems/difference-between-element-sum-and-digit-sum-of-an-array) [我的代码](2535.difference_between_element_sum_and_digit_sum_of_an_array.py)

给你一个正整数数组 <code>nums</code> 。

<ul>
	<li><strong>元素和</strong> 是 <code>nums</code> 中的所有元素相加求和。</li>
	<li><strong>数字和</strong> 是<code>nums</code> 中每一个元素的每一数位（重复数位需多次求和）相加求和。</li>
</ul>

返回 <strong>元素和</strong> 与 <strong>数字和</strong> 的绝对差。

<strong>注意：</strong>两个整数 <code>x</code> 和 <code>y</code> 的绝对差定义为 <code>|x - y|</code> 。



<strong>示例 1：</strong>

<pre>
<strong>输入：</strong>nums = [1,15,6,3]
<strong>输出：</strong>9
<strong>解释：</strong>
nums 的元素和是 1 + 15 + 6 + 3 = 25 。
nums 的数字和是 1 + 1 + 5 + 6 + 3 = 16 。
元素和与数字和的绝对差是 |25 - 16| = 9 。
</pre>

<strong>示例 2：</strong>

<pre>
<strong>输入：</strong>nums = [1,2,3,4]
<strong>输出：</strong>0
<strong>解释：</strong>
nums 的元素和是 1 + 2 + 3 + 4 = 10 。
nums 的数字和是 1 + 2 + 3 + 4 = 10 。
元素和与数字和的绝对差是 |10 - 10| = 0 。
</pre>



<strong>提示：</strong>

<ul>
	<li><code>1 <= nums.length <= 2000</code></li>
	<li><code>1 <= nums[i] <= 2000</code></li>
</ul>

## 2536.子矩阵元素加 1

[打开力扣](https://leetcode.cn/problems/increment-submatrices-by-one) [我的代码](2536.increment_submatrices_by_one.py)

给你一个正整数 <code>n</code> ，表示最初有一个 <code>n x n</code> 、下标从 <strong>0</strong> 开始的整数矩阵 <code>mat</code> ，矩阵中填满了 0 。

另给你一个二维整数数组 <code>query</code> 。针对每个查询 <code>query[i] = [row1<sub>i</sub>, col1<sub>i</sub>, row2<sub>i</sub>, col2<sub>i</sub>]</code> ，请你执行下述操作：

<ul>
	<li>找出 <strong>左上角</strong> 为 <code>(row1<sub>i</sub>, col1<sub>i</sub>)</code> 且 <strong>右下角</strong> 为 <code>(row2<sub>i</sub>, col2<sub>i</sub>)</code> 的子矩阵，将子矩阵中的 <strong>每个元素</strong> 加 <code>1</code> 。也就是给所有满足 <code>row1<sub>i</sub> <= x <= row2<sub>i</sub></code> 和 <code>col1<sub>i</sub> <= y <= col2<sub>i</sub></code> 的 <code>mat[x][y]</code> 加 <code>1</code> 。</li>
</ul>

返回执行完所有操作后得到的矩阵 <code>mat</code> 。



<strong>示例 1：</strong>

<img alt="" src="https://assets.leetcode.com/uploads/2022/11/24/p2example11.png" style="width: 531px; height: 121px;" />

<pre>
<strong>输入：</strong>n = 3, queries = [[1,1,2,2],[0,0,1,1]]
<strong>输出：</strong>[[1,1,0],[1,2,1],[0,1,1]]
<strong>解释：</strong>上图所展示的分别是：初始矩阵、执行完第一个操作后的矩阵、执行完第二个操作后的矩阵。
- 第一个操作：将左上角为 (1, 1) 且右下角为 (2, 2) 的子矩阵中的每个元素加 1 。
- 第二个操作：将左上角为 (0, 0) 且右下角为 (1, 1) 的子矩阵中的每个元素加 1 。
</pre>

<strong>示例 2：</strong>

<img alt="" src="https://assets.leetcode.com/uploads/2022/11/24/p2example22.png" style="width: 261px; height: 82px;" />

<pre>
<strong>输入：</strong>n = 2, queries = [[0,0,1,1]]
<strong>输出：</strong>[[1,1],[1,1]]
<strong>解释：</strong>上图所展示的分别是：初始矩阵、执行完第一个操作后的矩阵。
- 第一个操作：将矩阵中的每个元素加 1 。</pre>



<strong>提示：</strong>

<ul>
	<li><code>1 <= n <= 500</code></li>
	<li><code>1 <= queries.length <= 10<sup>4</sup></code></li>
	<li><code>0 <= row1<sub>i</sub> <= row2<sub>i</sub> < n</code></li>
	<li><code>0 <= col1<sub>i</sub> <= col2<sub>i</sub> < n</code></li>
</ul>

## 2537.统计好子数组的数目

[打开力扣](https://leetcode.cn/problems/count-the-number-of-good-subarrays) [我的代码](2537.count_the_number_of_good_subarrays.py)

给你一个整数数组 <code>nums</code>和一个整数 <code>k</code>，请你返回 <code>nums</code>中 <strong>好</strong>子数组的数目。

一个子数组 <code>arr</code>如果有 <strong>至少</strong><code>k</code>对下标 <code>(i, j)</code>满足 <code>i < j</code>且 <code>arr[i] == arr[j]</code>，那么称它是一个 <strong>好</strong>子数组。

<strong>子数组</strong>是原数组中一段连续 <strong>非空</strong>的元素序列。



<strong>示例 1：</strong>

<pre><b>输入：</b>nums = [1,1,1,1,1], k = 10
<b>输出：</b>1
<b>解释：</b>唯一的好子数组是这个数组本身。
</pre>

<strong>示例 2：</strong>

<pre><b>输入：</b>nums = [3,1,4,3,2,2,4], k = 2
<b>输出：</b>4
<b>解释：</b>总共有 4 个不同的好子数组：
- [3,1,4,3,2,2] 有 2 对。
- [3,1,4,3,2,2,4] 有 3 对。
- [1,4,3,2,2,4] 有 2 对。
- [4,3,2,2,4] 有 2 对。
</pre>



<strong>提示：</strong>

<ul>
	<li><code>1 <= nums.length <= 10<sup>5</sup></code></li>
	<li><code>1 <= nums[i], k <= 10<sup>9</sup></code></li>
</ul>

## 2538.最大价值和与最小价值和的差值

[打开力扣](https://leetcode.cn/problems/difference-between-maximum-and-minimum-price-sum) [我的代码](2538.difference_between_maximum_and_minimum_price_sum.py)

给你一个 <code>n</code>个节点的无向无根图，节点编号为<code>0</code>到<code>n - 1</code>。给你一个整数<code>n</code>和一个长度为 <code>n - 1</code>的二维整数数组<code>edges</code>，其中<code>edges[i] = [a<sub>i</sub>, b<sub>i</sub>]</code>表示树中节点<code>a<sub>i</sub></code> 和<code>b<sub>i</sub></code>之间有一条边。

每个节点都有一个价值。给你一个整数数组<code>price</code>，其中<code>price[i]</code>是第 <code>i</code>个节点的价值。

一条路径的 <strong>价值和</strong>是这条路径上所有节点的价值之和。

你可以选择树中任意一个节点作为根节点<code>root</code>。选择 <code>root</code>为根的 <strong>开销</strong>是以 <code>root</code>为起点的所有路径中，<strong>价值和</strong>最大的一条路径与最小的一条路径的差值。

请你返回所有节点作为根节点的选择中，<strong>最大</strong>的 <strong>开销</strong>为多少。



<strong>示例 1：</strong>

<img alt="" src="https://assets.leetcode.com/uploads/2022/12/01/example14.png" style="width: 556px; height: 231px;" />

<pre>
<b>输入：</b>n = 6, edges = [[0,1],[1,2],[1,3],[3,4],[3,5]], price = [9,8,7,6,10,5]
<b>输出：</b>24
<b>解释：</b>上图展示了以节点 2 为根的树。左图（红色的节点）是最大价值和路径，右图（蓝色的节点）是最小价值和路径。
- 第一条路径节点为 [2,1,3,4]：价值为 [7,8,6,10] ，价值和为 31 。
- 第二条路径节点为 [2] ，价值为 [7] 。
最大路径和与最小路径和的差值为 24 。24 是所有方案中的最大开销。
</pre>

<strong>示例 2：</strong>

<img alt="" src="https://assets.leetcode.com/uploads/2022/11/24/p1_example2.png" style="width: 352px; height: 184px;" />

<pre>
<b>输入：</b>n = 3, edges = [[0,1],[1,2]], price = [1,1,1]
<b>输出：</b>2
<b>解释：</b>上图展示了以节点 0 为根的树。左图（红色的节点）是最大价值和路径，右图（蓝色的节点）是最小价值和路径。
- 第一条路径包含节点 [0,1,2]：价值为 [1,1,1] ，价值和为 3 。
- 第二条路径节点为 [0] ，价值为 [1] 。
最大路径和与最小路径和的差值为 2 。2 是所有方案中的最大开销。
</pre>



<strong>提示：</strong>

<ul>
	<li><code>1 <= n <= 10<sup>5</sup></code></li>
	<li><code>edges.length == n - 1</code></li>
	<li><code>0 <= a<sub>i</sub>, b<sub>i</sub> <= n - 1</code></li>
	<li><code>edges</code> 表示一棵符合题面要求的树。</li>
	<li><code>price.length == n</code></li>
	<li><code>1 <= price[i] <= 10<sup>5</sup></code></li>
</ul>
