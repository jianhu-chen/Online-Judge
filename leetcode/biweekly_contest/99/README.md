# 第 99 场双周赛

> 企业: Optiver

## 6312.最小和分割

[打开力扣](https://leetcode.cn/problems/split-with-minimum-sum) [我的代码](6312.split_with_minimum_sum.py)

给你一个正整数<code>num</code>，请你将它分割成两个非负整数<code>num1</code> 和<code>num2</code>，满足：

<ul>
	<li><code>num1</code> 和<code>num2</code>直接连起来，得到<code>num</code>各数位的一个排列。

	<ul>
		<li>换句话说，<code>num1</code> 和<code>num2</code>中所有数字出现的次数之和等于<code>num</code>中所有数字出现的次数。</li>
	</ul>
	</li>
	<li><code>num1</code> 和<code>num2</code>可以包含前导 0 。</li>
</ul>

请你返回<code>num1</code> 和 <code>num2</code>可以得到的和的 <strong>最小</strong> 值。

<strong>注意：</strong>

<ul>
	<li><code>num</code>保证没有前导 0 。</li>
	<li><code>num1</code> 和<code>num2</code>中数位顺序可以与<code>num</code>中数位顺序不同。</li>
</ul>



<strong>示例 1：</strong>

<pre>
<b>输入：</b>num = 4325
<b>输出：</b>59
<b>解释：</b>我们可以将 4325 分割成 <code>num1 </code>= 24 和 num2<code> = </code>35 ，和为 59 ，59 是最小和。
</pre>

<strong>示例 2：</strong>

<pre>
<b>输入：</b>num = 687
<b>输出：</b>75
<b>解释：</b>我们可以将 687 分割成 <code>num1</code> = 68 和 <code>num2 </code>= 7 ，和为最优值 75 。
</pre>



<strong>提示：</strong>

<ul>
	<li><code>10 <= num <= 10<sup>9</sup></code></li>
</ul>

## 6311.统计染色格子数

[打开力扣](https://leetcode.cn/problems/count-total-number-of-colored-cells) [我的代码](6311.count_total_number_of_colored_cells.py)

有一个无穷大的二维网格图，一开始所有格子都未染色。给你一个正整数<code>n</code>，表示你需要执行以下步骤<code>n</code>分钟：

<ul>
	<li>第一分钟，将 <strong>任一</strong> 格子染成蓝色。</li>
	<li>之后的每一分钟，将与蓝色格子相邻的 <strong>所有</strong> 未染色格子染成蓝色。</li>
</ul>

下图分别是 1、2、3 分钟后的网格图。
<img alt="" src="https://assets.leetcode.com/uploads/2023/01/10/example-copy-2.png" style="width: 500px; height: 279px;">
请你返回 <code>n</code>分钟之后 <strong>被染色的格子</strong>数目。



<b>示例 1：</b>

<pre><b>输入：</b>n = 1
<b>输出：</b>1
<b>解释：</b>1 分钟后，只有 1 个蓝色的格子，所以返回 1 。
</pre>

<strong>示例 2：</strong>

<pre><b>输入：</b>n = 2
<b>输出：</b>5
<b>解释：</b>2 分钟后，有 4 个在边缘的蓝色格子和 1 个在中间的蓝色格子，所以返回 5 。
</pre>



<strong>提示：</strong>

<ul>
	<li><code>1 <= n <= 10<sup>5</sup></code></li>
</ul>

## 6313.统计将重叠区间合并成组的方案数

[打开力扣](https://leetcode.cn/problems/count-ways-to-group-overlapping-ranges) [我的代码](6313.count_ways_to_group_overlapping_ranges.py)

给你一个二维整数数组<code>ranges</code>，其中<code>ranges[i] = [start<sub>i</sub>, end<sub>i</sub>]</code>表示<code>start<sub>i</sub></code>到<code>end<sub>i</sub></code>之间（包括二者）的所有整数都包含在第<code>i</code>个区间中。

你需要将<code>ranges</code>分成 <strong>两个</strong>组（可以为空），满足：

<ul>
	<li>每个区间只属于一个组。</li>
	<li>两个有 <strong>交集</strong>的区间必须在 <strong>同一个</strong>组内。</li>
</ul>

如果两个区间有至少 <strong>一个</strong>公共整数，那么这两个区间是 <b>有交集</b>的。

<ul>
	<li>比方说，区间<code>[1, 3]</code> 和<code>[2, 5]</code>有交集，因为<code>2</code>和<code>3</code>在两个区间中都被包含。</li>
</ul>

请你返回将 <code>ranges</code>划分成两个组的 <strong>总方案数</strong>。由于答案可能很大，将它对<code>10<sup>9</sup> + 7</code><strong>取余</strong>后返回。



<strong>示例 1：</strong>

<pre><b>输入：</b>ranges = [[6,10],[5,15]]
<b>输出：</b>2
<b>解释：</b>
两个区间有交集，所以它们必须在同一个组内。
所以有两种方案：
- 将两个区间都放在第 1 个组中。
- 将两个区间都放在第 2 个组中。
</pre>

<strong>示例 2：</strong>

<pre><b>输入：</b>ranges = [[1,3],[10,20],[2,5],[4,8]]
<b>输出：</b>4
<b>解释：</b>
区间 [1,3] 和 [2,5] 有交集，所以它们必须在同一个组中。
同理，区间 [2,5] 和 [4,8] 也有交集，所以它们也必须在同一个组中。
所以总共有 4 种分组方案：
- 所有区间都在第 1 组。
- 所有区间都在第 2 组。
- 区间 [1,3] ，[2,5] 和 [4,8] 在第 1 个组中，[10,20] 在第 2 个组中。
- 区间 [1,3] ，[2,5] 和 [4,8] 在第 2 个组中，[10,20] 在第 1 个组中。
</pre>



<strong>提示：</strong>

<ul>
	<li><code>1 <= ranges.length <= 10<sup>5</sup></code></li>
	<li><code>ranges[i].length == 2</code></li>
	<li><code>0 <= start<sub>i</sub> <= end<sub>i</sub> <= 10<sup>9</sup></code></li>
</ul>

## 6314.统计可能的树根数目

[打开力扣](https://leetcode.cn/problems/count-number-of-possible-root-nodes) [我的代码](6314.count_number_of_possible_root_nodes.py)

Alice 有一棵 <code>n</code> 个节点的树，节点编号为 <code>0</code> 到 <code>n - 1</code> 。树用一个长度为 <code>n - 1</code> 的二维整数数组 <code>edges</code> 表示，其中 <code>edges[i] = [a<sub>i</sub>, b<sub>i</sub>]</code> ，表示树中节点 <code>a<sub>i</sub></code> 和 <code>b<sub>i</sub></code> 之间有一条边。

Alice 想要 Bob 找到这棵树的根。她允许 Bob 对这棵树进行若干次 <strong>猜测</strong> 。每一次猜测，Bob 做如下事情：

<ul>
	<li>选择两个 <strong>不相等</strong>的整数<code>u</code> 和<code>v</code>，且树中必须存在边<code>[u, v]</code>。</li>
	<li>Bob 猜测树中<code>u</code>是<code>v</code>的 <strong>父节点</strong>。</li>
</ul>

Bob 的猜测用二维整数数组<code>guesses</code> 表示，其中<code>guesses[j] = [u<sub>j</sub>, v<sub>j</sub>]</code>表示 Bob 猜<code>u<sub>j</sub></code> 是<code>v<sub>j</sub></code>的父节点。

Alice 非常懒，她不想逐个回答Bob 的猜测，只告诉 Bob 这些猜测里面 <strong>至少</strong>有<code>k</code>个猜测的结果为<code>true</code>。

给你二维整数数组 <code>edges</code>，Bob 的所有猜测和整数<code>k</code>，请你返回可能成为树根的<strong>节点数目</strong>。如果没有这样的树，则返回 <code>0</code>。



<strong>示例 1：</strong>

<img alt="" src="https://assets.leetcode.com/uploads/2022/12/19/ex-1.png" style="width: 727px; height: 250px;" />

<pre>
<b>输入：</b>edges = [[0,1],[1,2],[1,3],[4,2]], guesses = [[1,3],[0,1],[1,0],[2,4]], k = 3
<b>输出：</b>3
<b>解释：</b>
根为节点 0 ，正确的猜测为 [1,3], [0,1], [2,4]
根为节点 1 ，正确的猜测为 [1,3], [1,0], [2,4]
根为节点 2 ，正确的猜测为 [1,3], [1,0], [2,4]
根为节点 3 ，正确的猜测为 [1,0], [2,4]
根为节点 4 ，正确的猜测为 [1,3], [1,0]
节点 0 ，1 或 2 为根时，可以得到 3 个正确的猜测。
</pre>

<strong>示例 2：</strong>

<img alt="" src="https://assets.leetcode.com/uploads/2022/12/19/ex-2.png" style="width: 600px; height: 303px;" />

<pre>
<b>输入：</b>edges = [[0,1],[1,2],[2,3],[3,4]], guesses = [[1,0],[3,4],[2,1],[3,2]], k = 1
<b>输出：</b>5
<b>解释：</b>
根为节点 0 ，正确的猜测为 [3,4]
根为节点 1 ，正确的猜测为 [1,0], [3,4]
根为节点 2 ，正确的猜测为 [1,0], [2,1], [3,4]
根为节点 3 ，正确的猜测为 [1,0], [2,1], [3,2], [3,4]
根为节点 4 ，正确的猜测为 [1,0], [2,1], [3,2]
任何节点为根，都至少有 1 个正确的猜测。
</pre>



<strong>提示：</strong>

<ul>
	<li><code>edges.length == n - 1</code></li>
	<li><code>2 <= n <= 10<sup>5</sup></code></li>
	<li><code>1 <= guesses.length <= 10<sup>5</sup></code></li>
	<li><code>0 <= a<sub>i</sub>, b<sub>i</sub>, u<sub>j</sub>, v<sub>j</sub> <= n - 1</code></li>
	<li><code>a<sub>i</sub> != b<sub>i</sub></code></li>
	<li><code>u<sub>j</sub> != v<sub>j</sub></code></li>
	<li><code>edges</code>表示一棵有效的树。</li>
	<li><code>guesses[j]</code>是树中的一条边。</li>
	<li><code>0 <= k <= guesses.length</code></li>
</ul>
