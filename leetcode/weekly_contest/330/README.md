# 第 330 场周赛

> 企业: 力扣

## 2549.统计桌面上的不同数字

[打开力扣](https://leetcode.cn/problems/count-distinct-numbers-on-board) [我的代码](2549.count_distinct_numbers_on_board.py)

给你一个正整数 <code>n</code> ，开始时，它放在桌面上。在 <code>10<sup>9</sup></code> 天内，每天都要执行下述步骤：

<ul>
	<li>对于出现在桌面上的每个数字 <code>x</code> ，找出符合 <code>1 <= i <= n</code> 且满足 <code>x % i == 1</code> 的所有数字 <code>i</code> 。</li>
	<li>然后，将这些数字放在桌面上。</li>
</ul>

返回在 <code>10<sup>9</sup></code> 天之后，出现在桌面上的 <strong>不同</strong> 整数的数目。

<strong>注意：</strong>

<ul>
	<li>一旦数字放在桌面上，则会一直保留直到结束。</li>
	<li><code>%</code> 表示取余运算。例如，<code>14 % 3</code> 等于 <code>2</code> 。</li>
</ul>



<strong>示例 1：</strong>

<pre>
<strong>输入：</strong>n = 5
<strong>输出：</strong>4
<strong>解释：</strong>最开始，5 在桌面上。
第二天，2 和 4 也出现在桌面上，因为 5 % 2 == 1 且 5 % 4 == 1 。
再过一天 3 也出现在桌面上，因为 4 % 3 == 1 。
在十亿天结束时，桌面上的不同数字有 2 、3 、4 、5 。
</pre>

<strong>示例 2：</strong>

<pre>
<strong>输入：</strong>n = 3
<strong>输出：</strong>2
<strong>解释：</strong>
因为 3 % 2 == 1 ，2 也出现在桌面上。
在十亿天结束时，桌面上的不同数字只有两个：2 和 3 。
</pre>



<strong>提示：</strong>

<ul>
	<li><code>1 <= n <= 100</code></li>
</ul>

## 2550.猴子碰撞的方法数

[打开力扣](https://leetcode.cn/problems/count-collisions-of-monkeys-on-a-polygon) [我的代码](2550.count_collisions_of_monkeys_on_a_polygon.py)

现在有一个正凸多边形，其上共有 <code>n</code> 个顶点。顶点按顺时针方向从 <code>0</code> 到 <code>n - 1</code> 依次编号。每个顶点上 <strong>正好有一只猴子</strong> 。下图中是一个 6 个顶点的凸多边形。

<img alt="" src="https://assets.leetcode.com/uploads/2023/01/22/hexagon.jpg" style="width: 300px; height: 293px;">

每个猴子同时移动到相邻的顶点。顶点 <code>i</code> 的相邻顶点可以是：

<ul>
	<li>顺时针方向的顶点 <code>(i + 1) % n</code> ，或</li>
	<li>逆时针方向的顶点 <code>(i - 1 + n) % n</code> 。</li>
</ul>

如果移动后至少有两个猴子位于同一顶点，则会发生 <strong>碰撞</strong> 。

返回猴子至少发生 <strong>一次碰撞 </strong>的移动方法数。由于答案可能非常大，请返回对 <code>10<sup>9</sup>+7</code> 取余后的结果。

<strong>注意</strong>，每只猴子只能移动一次。



<strong>示例 1：</strong>

<pre><strong>输入：</strong>n = 3
<strong>输出：</strong>6
<strong>解释：</strong>共计 8 种移动方式。
下面列出两种会发生碰撞的方式：
- 猴子 1 顺时针移动；猴子 2 逆时针移动；猴子 3 顺时针移动。猴子 1 和猴子 2 碰撞。
- 猴子 1 逆时针移动；猴子 2 逆时针移动；猴子 3 顺时针移动。猴子 1 和猴子 3 碰撞。
可以证明，有 6 种让猴子碰撞的方法。
</pre>

<strong>示例 2：</strong>

<pre><strong>输入：</strong>n = 4
<strong>输出：</strong>14
<strong>解释：</strong>可以证明，有 14 种让猴子碰撞的方法。</pre>



<strong>提示：</strong>

<ul>
	<li><code>3 <= n <= 10<sup>9</sup></code></li>
</ul>

## 2551.将珠子放入背包中

[打开力扣](https://leetcode.cn/problems/put-marbles-in-bags) [我的代码](2551.put_marbles_in_bags.py)

你有<code>k</code>个背包。给你一个下标从 <strong>0</strong>开始的整数数组<code>weights</code>，其中<code>weights[i]</code>是第<code>i</code>个珠子的重量。同时给你整数 <code>k</code>。

请你按照如下规则将所有的珠子放进<code>k</code>个背包。

<ul>
	<li>没有背包是空的。</li>
	<li>如果第<code>i</code>个珠子和第<code>j</code>个珠子在同一个背包里，那么下标在<code>i</code>到<code>j</code>之间的所有珠子都必须在这同一个背包中。</li>
	<li>如果一个背包有下标从<code>i</code>到<code>j</code>的所有珠子，那么这个背包的价格是<code>weights[i] + weights[j]</code>。</li>
</ul>

一个珠子分配方案的 <strong>分数</strong>是所有 <code>k</code>个背包的价格之和。

请你返回所有分配方案中，<strong>最大分数</strong>与 <strong>最小分数</strong>的 <strong>差值</strong>为多少。



<strong>示例 1：</strong>

<pre><b>输入：</b>weights = [1,3,5,1], k = 2
<b>输出：</b>4
<b>解释：</b>
分配方案 [1],[3,5,1] 得到最小得分 (1+1) + (3+1) = 6 。
分配方案 [1,3],[5,1] 得到最大得分 (1+3) + (5+1) = 10 。
所以差值为 10 - 6 = 4 。
</pre>

<strong>示例 2：</strong>

<pre><b>输入：</b>weights = [1, 3], k = 2
<b>输出：</b>0
<b>解释：</b>唯一的分配方案为 [1],[3] 。
最大最小得分相等，所以返回 0 。
</pre>



<strong>提示：</strong>

<ul>
	<li><code>1 <= k <= weights.length <= 10<sup>5</sup></code></li>
	<li><code>1 <= weights[i] <= 10<sup>9</sup></code></li>
</ul>

## 2552.统计上升四元组

[打开力扣](https://leetcode.cn/problems/count-increasing-quadruplets) [我的代码](2552.count_increasing_quadruplets.py)

给你一个长度为 <code>n</code>下标从 <strong>0</strong>开始的整数数组<code>nums</code>，它包含<code>1</code>到<code>n</code>的所有数字，请你返回上升四元组的数目。

如果一个四元组<code>(i, j, k, l)</code>满足以下条件，我们称它是上升的：

<ul>
	<li><code>0 <= i < j < k < l < n</code>且</li>
	<li><code>nums[i] < nums[k] < nums[j] < nums[l]</code>。</li>
</ul>



<strong>示例 1：</strong>

<pre><b>输入：</b>nums = [1,3,2,4,5]
<b>输出：</b>2
<b>解释：</b>
- 当 i = 0 ，j = 1 ，k = 2 且 l = 3 时，有 nums[i] < nums[k] < nums[j] < nums[l] 。
- 当 i = 0 ，j = 1 ，k = 2 且 l = 4 时，有 nums[i] < nums[k] < nums[j] < nums[l] 。
没有其他的四元组，所以我们返回 2 。
</pre>

<strong>示例 2：</strong>

<pre><b>输入：</b>nums = [1,2,3,4]
<b>输出：</b>0
<b>解释：</b>只存在一个四元组 i = 0 ，j = 1 ，k = 2 ，l = 3 ，但是 nums[j] < nums[k] ，所以我们返回 0 。
</pre>



<strong>提示：</strong>

<ul>
	<li><code>4 <= nums.length <= 4000</code></li>
	<li><code>1 <= nums[i] <= nums.length</code></li>
	<li><code>nums</code>中所有数字 <strong>互不相同</strong>，<code>nums</code>是一个排列。</li>
</ul>
